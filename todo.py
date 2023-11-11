import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(
            label='I love Sana Sunomiya <3',
            expand=True
        )
        add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=self.add_new_task
        )
        self.tasks_list = ft.Column()
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        add_button
                    ]
                ),
                self.tasks_list
            ]
        )
    
    def add_new_task(self, e):
        new_task_class = Task(self.new_task.value)
        self.new_task.value = ''
        self.tasks_list.controls.append(new_task_class)
        self.update()
        
class Task(ft.UserControl):
    def __init__(self, task_name):
        super().__init__()
        self.task_name = task_name
        
    def build(self):
        self.edited_task = ft.TextField(value=self.task_name)
        self.task = ft.Checkbox(label=self.task_name)
        self.task_view = ft.Row(
            controls=[
                self.task,
                ft.FilledButton(text='Edit', on_click=self.edit),
                ft.FilledButton(text='Delete'),
            ]
        )
        self.edit_view = ft.Row(
            visible=False,
                controls=[
                self.edited_task,
                ft.FilledButton(text='Save', on_click=self.save)  
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
    
def main(page: ft.Page):
    page.title = 'ToDO'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    todo = TodoApp()
    page.add(todo)

ft.app(target=main)