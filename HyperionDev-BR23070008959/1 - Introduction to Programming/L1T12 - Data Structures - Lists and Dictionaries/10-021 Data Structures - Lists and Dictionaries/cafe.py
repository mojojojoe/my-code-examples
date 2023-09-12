#!/usr/bin/env python3
""""
Note to lecturer: sorry about the overkill, I am practising OOP, an area I need to work on.
I am also trying to develop strategic skills. If you have any insight into the topic I would
definitely be all ears. 
"""
class Cafe():
    """
    Cafe: a class to hold a restaurants menu, to hold the associated stock and the price. Also 
    included is a function to tally the stock value.
    """
    def __init__(self):
    # data structures to hold data. Note that each structure is immutable???
        self.menu = []
        self.stock = {}
        self.price = {}
        
    def add_to_menu(self, item):
        self.menu.append(item)
             
    def set_stock(self, item: str, num: int):
        self.stock[item] = num
        
    def set_price(self,item:str,amnt:float):
        self.price[item] = amnt
      
    def calc_total_value(self)->float:
        """
        Tallies the total stock value based on inventory and value. 
        Returns:
            float: the total stock value
        """
        tally = 0
        for item in self.menu:
            tally += self.stock[item] * self.price[item]
        return tally
        
    def create_entry(self, item: str, num: int, amnt: float):
        """"
        Takes the item, its number and its amount and populates the class data structures.
        """
        self.add_to_menu(item)
        self.set_stock(item, num)
        self.set_price(item, amnt)

def main():
    """
    Implements the Cafe class, and populates the data structures. Finally calculates 
    the stock value with the function from the class.
    """
    cafe = Cafe()
    cafe.create_entry('English breakfast', 40, 65.0)
    cafe.create_entry('French toast', 50, 35.0)
    cafe.create_entry('Coffee', 100, 25.0)
    print(cafe.calc_total_value())
    
if __name__ == '__main__':
    main()