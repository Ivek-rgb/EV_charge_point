import time
from requests import Response, get
import rest_framework.response as django_response
import json 
import random
import threading
from winsound import Beep  # Za Windows

class RequestFailedException(Exception): 
    def __init__(self, message, status_code):
        self.message = f"{message} - request failed with status code {status_code}" 
        super().__init__(self.message) 

class ChargerManager: 

    # ** STATIC DATA THAT WILL NOT BE CHANGED  **
    url = "https://hr.rechargespots.eu/DuskyWebApi//noauthlocation"

    def __init__(self): 
        self.last_available = None
        self.last_occupied = None
        self.const_params = {
            "isOldApi": "false",
            "UiCulture": "hr-HR"
        }
    
    def __get_one_charger_info(self, id) -> Response: 
        self.const_params["Id"] = id
        response = get(url=ChargerManager.url, params=self.const_params)
        # further response handling if needed 
        return response
    
    def handle_charger_available(self, id) -> Response | None: 
        charger_response = self.__get_one_charger_info(id)
        if charger_response.status_code == 200:
            
            data = charger_response.json()  
            available = data.get("AvailableEvses")
            occupied = data.get("OccupiedEvses")
            
            if available != self.last_available or occupied != self.last_occupied: 
               
                self.last_available = available
                self.last_occupied = occupied

                ret_msg = f"slobodno: {available} zauzeto: {occupied}"
                return django_response.Response({"charger_status":ret_msg})
            else: return django_response.Response({"charger_status" : f"slobodno: {self.last_available} zauzeto: {self.last_occupied}"})
        else:
            print(f"Failure - request failed with status code {charger_response.status_code}") 
            response =  django_response.Response({"message":"error with establishing connection to charger tracker api"}) 
            response.status_code = 500
            return response
        pass        
        
    def dummy_function(): 
        pass
