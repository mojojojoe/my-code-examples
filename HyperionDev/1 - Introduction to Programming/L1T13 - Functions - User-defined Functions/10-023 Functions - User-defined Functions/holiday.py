#!/usr/bin/env python3

"""
This program is buggy and lacks functionality but provides the basic functions asked for.
I found the easiest way to bring it together was in a class.
"""

import os
import time

class Travel :
    """
    A class to implement travel cost calculations and all information gathering aspects to this task
    """
    def __init__ (self, destination = ''):
        """
        Initialize all the variables
        """              
        self.city_cost_dict = {'Cape Town': 12000,
                               'Johannesburg': 5000,
                               'Pretoria': 2000}
        self.hotel_rate = 500
        self.car_rate = 125
        self.destination = destination
        self.num_nights = 0
        self.rental_days = 0
        self.holiday_total = 0
       
    def __str__(self):
        dest = self.destination
        xport_cost = self.get_plane_cost()
        tot_cost = self.get_holiday_cost()
        hot_rt = self.get_hotel_cost()
        nights = self.num_nights
        days = self.rental_days
        car_rt = self.get_car_cost()  
        return f"""
                        TRAVEL COSTS
                                        
        Your trip to {dest} will cost R{tot_cost}. The cost of 
        the transport will be R{xport_cost} having a hotel charge of 
        R{hot_rt} for {nights} nights and a car rental charge of 
        R{car_rt} for {days} days.
        """ 

       
    def update_city (self):
        """
        Obtain the most pertinent inputs from the user
        """
        self.destination = input ("Please type in the new destination ")
        
    def update_days_hired (self):
        self.num_nights = int (input ("How many nights do you plan to be away?"))
        self.rental_days = int (input ("How many days of car rental do you want"))

    def get_hotel_cost (self):
        """
        Calculate the cost of the hotel
        """
        return int(self.hotel_rate * self.num_nights)
    
    def get_car_cost (self):
        """
        Calculate the cost of car rental
        """
        return int(self.car_rate * self.rental_days)

    def get_plane_cost (self):
        """
        Determine the cost of transport to a city

        Returns:
            the value of the city_cost_dict at city
            or zero if city is not a key in city cost dict
        """
        if self.destination in self.city_cost_dict:
            return int(self.city_cost_dict [self.destination]) 
        else:
            print ("Error: city not on list of possible destinations.")
            return 0
        
    def get_holiday_cost (self):
        """
        Calculates the overall cost of the travel
        """
        self.holiday_total =  self.get_plane_cost() + self.get_car_cost() + self.get_hotel_cost()
        return self.holiday_total
   
    def update_car_rate (self):
        """
        Update the car rental rate
        """
        os.system('clear')
        self.car_rate = input ("Type in the new car rental rate:  ")
        print("The car rate update is completed.")
        time.sleep(2)
            
    def update_hotel_rate (self):
        """
        Update the hotel room rate
        """
        os.system('clear')
        self.hotel_rate = input("Enter the hotel's rate")
        print("The hotel rate update is completed.")
        time.sleep(2)
        
    def update_city_dictionary (self):
        """
        Update the city_cost_dict with user input
        """
        os.system('clear')
        self.destination=input('Enter the new destination ')
        self.cost = int(input(f"Please provide the cost of travel to {self.destination}"))
        self.city_cost_dict[self.destination] = self.cost
        print(f"{self.destination} cost update is completed and set as {self.city_cost_dict[self.destination]}")
        time.sleep(5)

    def display_dict(self):
        """
        Display the information in city_cost_dict
        """
        for k in self.city_cost_dict.keys():
            print (k, self.city_cost_dict[k])
        
        time.sleep(5)





def main_menu (obj):
    """
    A loop which gives the user various options in a menu.
    Input is read and the corresponding function is executed.
    Returns:
        _type_: boolean
        _value_: True if successfully completed
    """
    main_menu_msg = """
    Please ensure that you complete 5 and 6 before exiting. 
    
        Press 2 to update the car rental rate
        Press 3 to update the hotel rate
        Press 4 to update the destination cost dictionary
        Press 5 to update car days rented and num nights in a hotel
        Press 6 to set a destination
        Press 7 to display the information in the dictionary
        Press any other key to generate a report
    """
    main_menu_choices = {
    # each function should return a string
        '2': obj.update_car_rate,
        '3': obj.update_hotel_rate,
        '4': obj.update_city_dictionary,
        '5': obj.update_days_hired,
        '6': obj.update_city,
        '7': obj.display_dict
    }   

    exit_loop = False
    while not exit_loop:
        os.system('clear')
        print(main_menu_msg)
        choice = input ("Please enter a choice:")
        if choice in main_menu_choices:
            print(main_menu_choices[choice]())
        else:
            print("Exiting. Bye....please wait for the report.")
            exit_loop = True
    return True



    
if __name__ == "__main__":
    hol1 = Travel(destination = 'Cape Town') 
    if main_menu(hol1): print(hol1)