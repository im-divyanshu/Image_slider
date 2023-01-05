# Import necessary stuff

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import  Clock
import os

#our layout class to define logic of the layout
#desgine logic is written in desgine.kv file
#desgine.kv

class MainWidget(Widget):
    # getting our current path

    dir=os.getcwd()
    os.chdir(dir)

    # defining important variables
    physics=False
    chemestry=False
    math=False
    count=1
    bcount=0
    a=0

    reset=False

    # initialazing our class
    # and getting all arguments

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.physics=False
        self.chemestry=False
        self.math=False
        Clock.schedule_interval(self.add,2.5)

    def add(self,dt):
        if(self.physics):
            self.change_image_phys()
        if(self.chemestry):
            self.change_image_chem()
        if(self.math):
            self.change_image_math()

    # functions called when buttons are pressed
    # enabling the buttons when start button is pressed
    
    def phys(self,dt):
        self.physics=True
        self.chemestry=False
        self.math=False

    def chem(self,dt):
        self.physics=False
        self.chemestry=True

        self.math=False
    def mat(self,dt):
        self.physics=False
        self.chemestry=False
        self.math=True

    # testing
    
    # def timedelay(self,dt):
    #     if(self.physics):
    #         self.change_image_phys
    #     if(self.chemestry):
    #         self.change_image_phys
    #     if(self.math):
    #         self.change_image_phys

    def change_sub(self):
        self.ids.phy.disabled=False
        self.ids.che.disabled=False
        self.ids.mat.disabled=False
        self.ids.cut.disabled=False
    
    # changing the image according to subject

    #pause
    def pause(self):
        self.statels=[self.physics,self.chemestry,self.math]
        self.physics=False
        self.chemestry=False
        self.math=False

    #resume
    def resume(self):
        self.physics=self.statels[0]
        self.chemestry=self.statels[1]
        self.math=self.statels[2]
 
    # physics Image
    def change_image_phys(self):
        os.chdir(f"{self.dir}\\physics")
        self.ls=os.listdir()
        if(self.count>=len(self.ls)):
            self.reset=True

        if(self.reset):
            self.count=0
            self.reset=False

        self.ids.image.source=self.dir+'\\physics\\'+self.ls[self.count]
        self.count+=1
    
    # chemestry Image
    def change_image_chem(self):
        os.chdir(f"{self.dir}\\chemestry")
        self.ls=os.listdir()
        if(self.count>=len(self.ls)):
            self.reset=True

        if(self.reset):
            self.count=0
            self.reset=False

        self.ids.image.source=self.dir+'\\chemestry\\'+self.ls[self.count]
        self.count+=1
    

    # math Image
    def change_image_math(self):
        os.chdir(f"{self.dir}\\math")
        self.ls=os.listdir()
        if(self.count>=len(self.ls)):
            self.reset=True

        if(self.reset):
            self.count=0
            self.reset=False
        #if self.id.example 

        self.ids.image.source=self.dir+'\\math\\'+self.ls[self.count]
        self.count+=1

    #disabling the Buttons when the cut is pressed 
    def cut(self):
        self.ids.phy.disabled=True
        self.ids.che.disabled=True
        self.ids.mat.disabled=True
        self.ids.cut.disabled=True
    
    def close_window(self):
        App.get_running_app().stop()
        Window.close()

#structure of the gui is defined by this string
#it's very important

kv=Builder.load_file('desgine.kv')

#app class used to define the name and some cheracterastics of app

class MainApp(App):
    def build(self):
        return kv

#at the end we are running our app

MainApp().run() 