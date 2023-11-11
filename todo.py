import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(
            label='Enter your item',
            expand=True
        )
        add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=self.add_new_task
        )
        self.tasks_list = ft.Column()
        self.filter = ft.Tabs(
            selected_index=1,
            on_change=self.tab_changed,
            tabs=[
                ft.Tab(text='All'),
                ft.Tab(text='Active'),
                ft.Tab(text='Completed'),
            ]
        )
        self.footer = ft.Text(f'Tasks remaining: 0')
        self.all_done = ft.Checkbox(label='Mark all as done', on_change=self.mark_all_done)
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        add_button
                    ]
                ),
                ft.Row(
                    controls=[
                        self.filter,
                        self.all_done,
                    ]
                ),
                self.tasks_list,
                ft.Row(
                    controls=[
                        self.footer,
                        ft.OutlinedButton(text='clear completed', on_click=self.clear_completed)
                    ]
                ),
            ]
        )
    
    def add_new_task(self, e):
        new_task_class = Task(self.new_task, self.delete_task, self.update)
        self.new_task.value = ''
        self.tasks_list.controls.append(new_task_class)
        self.update()
        
    def delete_task(self, task_reference):
        self.tasks_list.controls.remove(task_reference)
        self.update()
        
    def clear_completed(self, e):
        for task in self.tasks_list.controls[:]:
            if task.completed:
                self.tasks_list.controls.remove(task)
        self.update()
        
    def mark_all_done(self, e):
        for task in self.tasks_list.controls[:]:
            task.completed = self.all_done.value
            task.value = self.all_done.value
        self.update()
        
    def filtering(self):
        tasks_remaining = 0
        print('update')
        index = self.filter.selected_index
        for task in self.tasks_list.controls:
            task.visible = (
                index == 0
                or task.completed and index == 2
                or not task.completed and index == 1
            )
            if not task.completed:
                tasks_remaining += 1
        self.footer.value = f'Tasks remaining: {tasks_remaining}'
        
    def update(self):
        self.filtering()
        super().update()
    
    def tab_changed(self, e):
        self.update()
        
class Task(ft.UserControl):
    def __init__(self, task_reference, delete_reference, update_status_reference):
        super().__init__()
        self.task_name = task_reference.value
        self.delete_reference = delete_reference
        self.completed = False
        self.update_status = update_status_reference
        
    def build(self):
        self.edited_task = ft.TextField(value=self.task_name, expand=1)
        self.task = ft.Checkbox(label=self.task_name, expand=1, on_change=self.changed)
        self.task_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.task,
                ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit),
                ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete),
            ]
        )
        self.edit_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            visible=False,
                controls=[
                self.edited_task,
                ft.IconButton(icon=ft.icons.SAVE, on_click=self.save),
            ]
        )
        return ft.Column(
            controls=[
                self.task_view,
                self.edit_view
            ]
        )
    
    def edit(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()
        
    def save(self, e):
        self.task.label = self.edited_task.value
        self.edit_view.visible = False
        self.task_view.visible = True
        self.update()
        
    def delete(self, e):
        self.delete_reference(self)
        
    def changed(self, e):
        self.completed = self.task.value
        self.update_status()
    
def main(page: ft.Page):
    page.title = 'ToDO'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    todo = TodoApp()
    page.add(todo)

ft.app(target=main)