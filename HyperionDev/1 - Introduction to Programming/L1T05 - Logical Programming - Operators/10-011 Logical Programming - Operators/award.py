#!/usr/bin/env python3

def do_validations(s,c,r):
    pass

def ask_for_times():
    s = float(input("Please enter the swimming time: "))
    c = float(input("Please enter the cycling time: "))
    r = float(input("Please enter the running time: "))
    return s,c,r
#    do_validations(s,c,r)

def calc_tot(s:float,c:float,r:float)->int:
    return s+c+r
    
def display_award(time:int):
    qt = 100
    if time <= qt:
        print("You are awarded provincial colours!")
    elif time > qt and time <= qt + 5:
        print("You are awarded half colours!")
    elif time > qt + 5 and time <= qt + 10:
        print("You will be placed on the provincial scroll!")
    else:
        print("Bad luck, you never received an award!")
    
    
def award():
    display_award(calc_tot(ask_for_times()))

    
if __name__ == '__main__':
    award()