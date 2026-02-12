from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = (0, 0, 0, 1)

class MonarchSystem(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text="[ MONARCH SYSTEM ]", font_size='35sp', color=get_color_from_hex('#00FFFF'), bold=True))
        self.add_widget(Label(text="RANK: S-CLASS", font_size='22sp', color=(1, 1, 1, 1)))
        self.add_widget(Label(text="QUEST: 2KM RUN PROTOCOL", font_size='18sp', color=get_color_from_hex('#FF3333')))
        self.add_widget(Label(text="STATUS: SYNCHRONIZED", font_size='15sp', color=get_color_from_hex('#00FF00')))

class MonarchApp(App):
    def build(self):
        return MonarchSystem()

if __name__ == '__main__':
    MonarchApp().run()
