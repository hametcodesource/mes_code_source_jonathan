import imp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from sympy import false
from models import Pizza
from kivy.properties import NumericProperty,StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from http_client import HttpClient
from storage_manager import StorageManager
class PizzaWidget(BoxLayout):
    nom=StringProperty("")
    ingredients=StringProperty("")
    prix=NumericProperty(0)
    vagetarienne=BooleanProperty(False)


class MainWidget(FloatLayout):
    recycleView=ObjectProperty(None)
    error_str=StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """self.pizzas=[
            Pizza("4 Fromage","chevre,emantal,modzza,brie,conté",9.5,True),
            Pizza("Canibal","poulet,merguez,boeuf",11.5,False),
            Pizza("Calzone","fromage,jambon,champigons",10,True)

        ]"""

        HttpClient().get_pizzas(self.on_server_data,self.on_server_error)
    def on_parent(self,widget,parent):
        pizza_dic=StorageManager().load_data("pizzas")
        if pizza_dic:
            self.recycleView.data=pizza_dic

    def on_server_data(self,pizzas_dict):
        self.recycleView.data=pizzas_dict
        if len(pizzas_dict)!=0 :
            StorageManager().save_data("pizzas",pizzas_dict)
    
    def on_server_error(self,error):
        self.error_str="ERREUR: "+ error



class PizzaApp(App):
    pass



PizzaApp().run()