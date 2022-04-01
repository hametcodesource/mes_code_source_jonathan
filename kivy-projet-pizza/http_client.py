
from turtle import onclick
from kivy.network.urlrequest import UrlRequest
import json



class HttpClient():
    def get_pizzas(self,on_complete,on_error):
        url="https://pizzamadjango.herokuapp.com/api/GetPizzas"
        def data_receved(req, result):
            data=json.loads(result)
            pizzas_dict=[val['fields'] for val in data]
            #print(pizzas_dict)
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req,error):
            print('data_error')
            if on_error:
                on_error(str(error))

        def data_faillure(req,result):
            print('data_faillure')
            if on_error:
                on_error("Erreur serveur: "+str(req.resp_status))

        req = UrlRequest(url,on_success=data_receved,on_error=data_error,on_failure=data_faillure)