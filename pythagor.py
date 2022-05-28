from datetime import datetime
from kivy.metrics import dp
from data_manager import Date
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import SlideTransition

class Pythagor_table(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app

        save_data = Date()
        save_data = save_data.get_date()['current_date']

        self.orientation = 'vertical'

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Pythagor table', color='black', font_size=25)
        date = Label(text=f'Current date: {save_data}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(date)
        
        table = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.95, 0.5),
            column_data=[('', dp(5))] + [(str(i), dp(5)) for i in range(1,31)],
            rows_num=15,
            row_data=[
            ("[color=#ff0303]1[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]2[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]3[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]4[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]5[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]6[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]7[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]8[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]9[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]10[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]11[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]12[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),
            ("[color=#ff0303]13[/color]", "1", "2", "3",6,1,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5),],
        )

        individual = Button(text="Individual matrix")
        individual.bind(on_press=self.individual_button)

        input = Button(text="Input data", pos =(20, 20))
        input.bind(on_press=self.input_button)

        potential = Button(text="Potential graph", pos =(20, 20))
        potential.bind(on_press=self.potential_button)
        
        buttons = BoxLayout(padding=8, size_hint=(1, 0.08))
        buttons.add_widget(individual)
        buttons.add_widget(input)
        buttons.add_widget(potential)

        self.add_widget(header)
        self.add_widget(table)
        self.add_widget(buttons)
    
    def individual_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'right')
        self.__app.screen_manager.current = 'individual_matrix'

    def input_button(self, item):
        date = MDDatePicker()
        date.bind(on_save=self.set_date)
        date.open()

    def potential_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'potential_graph'

    def set_date(self, instance, value, date_range):
        save_date = Date()
        date: datetime = value
        save_date.set_date(
            year=date.year,
            month=date.month,
            day=date.day
        )
