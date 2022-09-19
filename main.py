import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
  #initialize infinity keywords
  def __init__(self, **kwargs):
    #call grid layout conatructor
    super(MyGridLayout, self).__init__(**kwargs)
    #set columm
    self.cols = 2
    # add widgets
    self.add_widget(Label(text="Name: "))
    # add input box
    self.name = TextInput(multiline=False)
    self.add_widget(self.name)
    # add widgets
    self.add_widget(Label(text="Favorite coffee : "))
    # add input box
    self.coffee = TextInput(multiline=False)
    self.add_widget(self.coffee)
    # add widgets
    self.add_widget(Label(text="Favorite color : "))
    # add input box
    self.color = TextInput(multiline=False)
    self.add_widget(self.color)
    # create submit button
    self.submit = Button(text="Submit", font_size=32)
    #bind the button 
    self.submit.bind(on_press=self.press)
    self.add_widget(self.submit)
    
  def press(self, instance):
    name = self.name.text
    coffee = self.coffee.text
    color = self.color.text
    self.add_widget(Label(text=f"Hallo {name}, coffee {coffee}, color {color}"))
    
    #clear the input box
    self.name.text = ""
    self.coffee.text = ""
    self.color.text = ""
    
class MyApp(App):
  def build(self):
    return MyGridLayout()

if __name__ == '__main__':
  MyApp().run()
  # TODO: write code...


