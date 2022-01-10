#imports
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition
from kivy.lang import Builder




#kivy code in a builder string :D
screen_manager = '''
ScreenManager:
    id: sm
    Login:
    Register
    Menu
<Login>:
    id: ls
    name: 'loginscreen'
    Image:
        source: 'logo'
        pos_hint:{"center_x":0.5,"center_y":0.83}
        size_hint:(0.5,0.3)
    MDLabel:
        id: loginbutton
        text: "Login"
        pos_hint:{"center_x": 0.5,"center_y": 0.63}
        halign: 'center'
        font_style: "H6"
        bold: True
    MDTextField:
        id: username
        hint_text:"Enter name"
        multiline: False
        halign:"left"
        pos_hint:{"center_x":0.5,"center_y":0.55}
        mode: "rectangle"
        size_hint:(0.54,0.1)
    MDTextField:
        id: password
        hint_text:"Enter password"
        color_mode: 'custom'
        helper_text: 'Required'
        multiline: False
        halign:"left"
        pos_hint:{"center_x":0.5,"center_y":0.44}
        mode: "rectangle"
        size_hint:(0.54,0.1)
    MDFillRoundFlatButton:
        id: submitbutton
        text:"Enter"
        pos_hint:{"center_x":0.5,"center_y":0.29}
        size_hint:(0.17,0.07)
        font_size:20
        on_press: 
            root.manager.current = 'menuscreen'

    MDIconButton:
        id: themechangerbutton
        icon: 'theme-light-dark'
        text: 'change theme'
        user_font_size:'30sp'
        pos_hint:{'center_x':0.026,"center_y":0.97}
        on_release: app.theme_changer()
        

       
<Register>:
    id : rs
    name: 'registerscreen'
    MDLabel:
        text: "register lol"
    
<Menu>:
    id: ms
    name: 'menuscreen'
    MDLabel:
        text: "Welcome"

'''     


#classes
class Login(Screen):
    pass


class Register(Screen):
    pass

class Menu(Screen):
    pass



#objects
screen_manager_object = ScreenManager(transition = SlideTransition())
screen_manager_object.add_widget(Login(name = 'loginscreen'))
screen_manager_object.add_widget(Register(name ='registerscreen'))
screen_manager_object.add_widget(Menu(name='menuscreen'))


#main class
class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        screen = Screen()
        screen_manager_variable = Builder.load_string(screen_manager)
        screen.add_widget(screen_manager_variable)
        return screen

    def theme_changer(self):
         if self.theme_cls.theme_style == 'Light':
             self.theme_cls.theme_style = 'Dark'

         else:
             self.theme_cls.theme_style ='Light'

if __name__ == "__main__":
    App().run()
