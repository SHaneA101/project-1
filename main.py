import json
from datetime import datetime, timedelta
from kivymd.app import MDApp
from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDFillRoundFlatButton
from datetime import datetime
from kivy.clock import Clock
from kivy.uix.label import Label
Window.size = 480 ,600
from kivy.uix.image import Image
from kivy.clock import Clock

KV = '''
ScreenManager:
    SplashScreen:
    MainScreen:
    RegisterScreen:
    HomeScreen:
    

<SplashScreen>:
    MDProgressBar:
        type: "determinate"
        running_duration: 1
        catching_duration: 1.5
    
    
<MainScreen>:
    name:"login"
    Image:
        radius: 24
        box_radius: [0, 0, 24, 24]
        box_color: 1, 1, 1, .2
        source: "unipack.png"
        pos_hint: {"center_x": .5, "center_y": .85}
        size_hint: None, None
        size: "450dp", "200dp"
        
    MDFloatLayout:
        MDLabel:
            text: "Login"
            pos_hint: {"center_y": .65}
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0,204/255,204/255,1
            
        MDLabel:
            text: "Welcome To Daily Attend"
            pos_hint: {"center_y": .60}
            font_style: "H6"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0,204/255,204/255,1
        
        MDTextField:
            id: email
            hint_text: "Enter Your Email"
            pos_hint: {"center_x":.5, "center_y":.50} 
            current_hint_text_color: 0,0,0,1
            size_hint_x: .8
            
        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x":.5, "center_y":.40} 
            current_hint_text_color: 0,0,0,1
            size_hint_x: .8
            password: True
        
        MDRaisedButton:
            text: "Log in"
            pos_hint: {"center_x":.5, "center_y":.25}
            size_hint_x: .5
            on_release: app.verify(email.text, password.text)
            on_press: root.manager.current = "home"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
            
        MDRaisedButton:
            id: "signin"
            text: "Sign in with google"
            icon_right: "google"
            pos_hint: {"center_x":.5, "center_y":.15}
            size_hint_x: .5
            on_release: app.login()
            theme_text_color: "Custom"
            text_color: 0,0,0,1
        
        MDFlatButton:
            text:"Register"
            custom_color: "White"
            pos_hint: {"center_x":.5}
            size_hint_x: .5
            on_press: root.manager.current = "register"
                
<RegisterScreen>:
    name: "register"
    MDFloatLayout:
        Image:
            source: "unipack.png"
            pos_hint: {"center_y": .85}
            
            
        MDLabel:
            text: "Sign Up To Daily Attend"
            pos_hint: {"center_x":.5, "center_y":.65}
            halign: "center"
            theme_text_color: "Primary"
            font_size: "22dp"

               
        MDTextField:
            id: fullname
            hint_text: "Full Name"
            pos_hint: {"center_x":.5, "center_y":.6}
            halign: "center"
            
        MDTextField:
            id: surname
            hint_text: "Surname"
            pos_hint: {"center_x":.5, "center_y":.5}
            halign: "center"
            
        MDTextField:
            id: id_Number
            hint_text: "ID Number"
            pos_hint: {"center_x":.5, "center_y":.4}
            halign: "center"
               
        MDTextField:
            id: email
            hint_text: "Email"
            pos_hint: {"center_x":.5, "center_y":.3}
            halign: "center"
                   
        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x":.5, "center_y":.2}
            halign: "center"
       
    MDFillRoundFlatButton:
        text: "Register"
        on_press: root.register_user()
        
        
        
<HomeScreen>:
    name: "home"
    Image:
        source: "unipack.png"
        pos_hint: {"center_x":.5,"center_y":.85}
        

    BoxLayout:
        oreintation: 'vertical'
        DataTableContent:
            id: data_table_content
    

    

'''

class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Add an image to the splash screen
        image = Image(source='morph.png')
        self.add_widget(image)
        
        # Schedule the function to switch screens after 2 seconds
        Clock.schedule_once(self.switch_screen, 5)

    def switch_screen(self, dt):
        # Function to switch to the main screen
        main_screen = BoxLayout(orientation='vertical')
        main_screen.add_widget(Label(text='Main Screen'))
        self.parent.current = "login"  # Switch to the login screen
    
class MainScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    def register_user(self):
        # Get user input data
        full_name = self.ids.fullname.text
        surname = self.ids.surname.text
        id_number = self.ids.id_Number.text
        email = self.ids.email.text
        password = self.ids.password.text

        # Create a dictionary to store user data
        user_data = {
            "full_name": full_name,
            "surname": surname,
            "id_number": id_number,
            "email": email,
            "password": password,
        }

        # Save user data to a JSON file
        filename = "user_data.json"
        try:
            with open(filename, "r") as file:
                # Load existing data
                existing_data = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty dictionary
            existing_data = {}

        # Add new user data to the existing data
        existing_data[email] = user_data

        # Write the updated data back to the file
        with open(filename, "w") as file:
            json.dump(existing_data, file)

        # Optionally, you can print a success message or navigate to another screen
        print(f"User {email} registered successfully!")
        self.manager.current = "login"
 
class DataTableContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
      
class HomeScreen(MDScreen):
    clock_in_data = []
    clock_out_data = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.clock_in_data = []
        self.clock_out_data = []
        
    def on_enter(self):
        self.get_all_time()
        
    def get_all_time(self):
        url = f"https://api.myjson.com/bins/{bin}"
        self.data_table = MDDataTable(
                size_hint=(6, .6),
                use_pagination=True,
                rows_num=20,
                column_data=[
                    ("Date", dp(10)),
                    ("Clock In", dp(20)),
                    ("Clock Out", dp(20)),
                    ("Total time worked", dp(20)),
                    ("Overtime worked", dp(20)),
                ],
            )
            
        self.add_widget(self.data_table)
        self.add_buttons()

    def add_buttons(self):
        # Adding "Clock In" button
        button_clock_in = MDFillRoundFlatButton(
            text="Clock In",
            pos_hint={"center_y":.65},
            on_release=self.clock_in,
        )

        # Adding "Clock Out" button
        button_clock_out = MDFillRoundFlatButton(
            text="Clock Out",
            pos_hint={"center_x": 0.28,"center_y": .65},
            on_release=self.clock_out,
        )
      

        # Adding buttons to the layout
        self.add_widget(button_clock_in)
        self.add_widget(button_clock_out)
        

    def clock_in(self, *args):
        self.clock_in_data.append(datetime.now())
        self.update_data_table()

    def clock_out(self, *args):
        self.clock_out_data.append(datetime.now())
        self.update_data_table()

    def update_data_table(self, clock_in=True):
        # Clearing previous data
        self.data_table.row_data = []

        # Merging clock-in and clock-out data
        combined_data = zip(self.clock_in_data, self.clock_out_data)

        # Adding data to the MDDataTable
        for clock_in, clock_out in combined_data:
            formatted_data = (
                clock_in.strftime("%Y-%m-%d"),
                clock_in.strftime("%I:%M %p") ,
                clock_out.strftime("%I:%M %p") if clock_out else "",
                self.calculate_total_time(clock_in, clock_out),
                self.calculate_overtime(clock_in, clock_out),
            )
            self.data_table.row_data.append(formatted_data)

        # If clock_in is True, update only the last clock-in row
        if clock_in and self.clock_in_data:
            last_clock_in = self.clock_in_data[-1]
            formatted_data = (
                last_clock_in.strftime("%Y-%m-%d"),
                last_clock_in.strftime("%I:%M %p"),
                "",# Clock Out is empty since it's a new Clock In
                "",# total Time worked is empty for a new Clock in
                "",# Overtime worked is empty for  a new Coclok in
            )
            self.data_table.row_data.append(formatted_data)
        data_to_save = {
        "clock_in_data": [str(dt) for dt in self.clock_in_data],
        "clock_out_data": [str(dt) for dt in self.clock_out_data],
    }

        with open("attendance_data.json", "w") as json_file:
            json.dump(data_to_save, json_file)
            
            
    def show_attendance(self):
        # You can add logic here to update the data in the MDDataTable
        print("Show attendance logic here...")
        
    def calculate_total_time(self, clock_in, clock_out):
        if clock_in and clock_out:
            time_worked = clock_out - clock_in
            return str(time_worked)
        return ""

    def calculate_overtime(self, clock_in, clock_out):
        # Add your overtime calculation logic here
        # For example, if overtime is calculated as hours beyond 8 hours:
        if clock_in and clock_out:
            standard_working_hours = timedelta(hours=8)
            time_worked = clock_out - clock_in
            overtime = max(time_worked - standard_working_hours, timedelta())
            return str(overtime)
        return ""            
class Attendance(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.title= "Daily Attend"
        self.icon = "icon.png"
        client_id = open("client_id.txt")
        client_secret = open("client_secret.txt")
        initialize_google(self.after_login, self.error_listener, client_id.read(), client_secret.read())
        kv= Builder.load_string(KV)
        return kv 
    
       
    def after_login(self,name,email,photo_uri):
        self.root.ids.label.text = f"Logged in as {name}"
        self.transition.direction = "left"
        self.root.current = "login"
        
    def error_listener(self):
        print("Logged in Faield!")
    
    def login(self):
        login_google()
        
    def logout(self):
        logout_google(self.after_logout)
    
    def after_logout(self):
        self.root.ids.label.text = ""
        self.transition.direction = "right"
        self.root.current = "login"
            
    def verify(self,email,password):
        if email == "123@gmail.com" and password == "1234":
            print("You are Logged in to Daily Attend")
    
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
           
if __name__ == "__main__":
    Attendance().run()