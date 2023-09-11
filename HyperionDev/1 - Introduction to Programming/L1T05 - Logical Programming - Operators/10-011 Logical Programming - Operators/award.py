#!/usr/bin/env python3

def do_validations(s,c,r):
    """
    Dummy function. To be used later to validate the user's input.
    """
    pass

def ask_for_times():
    """
    Take three inputs from the user at the terminal, the swimming, cycling and running 
    times of the user's triathlon results. Do validations on them and return the inputs.
    """
    s = int(input("Please enter the swimming time: "))
    c = int(input("Please enter the cycling time: "))
    r = int(input("Please enter the running time: "))
    do_validations(s,c,r)
    return s,c,r

def calc_tot(s:int, c:int, r:int)->int:
    """
    Just add the times together and return them.
    """
    return s+c+r
    
def obtain_award(time:int):
    """
    Work out what award the user will be awarded based on the input times. 
    The qualifying time is 100min. Compare this with the various achievement levels 
    and return a string of the result.
    """
    qt = 100
    if time <= qt:
        return "You are awarded provincial colours!"
    elif time > qt and time <= qt + 5:
        return "You are awarded half colours!"
    elif time > qt + 5 and time <= qt + 10:
        return "You will be placed on the provincial scroll!"
    else:
        return "Bad luck, you never received an award!"
    
    
def award():
    """
    Sew the functions together, asking for the times and printing out 
    the award obtained from the calculation.
    """
    s,c,r = ask_for_times()
    print(obtain_award(calc_tot(s,c,r)))

def test():
    """
    Test the document for different outcomes.
    """
    try:
        assert obtain_award(calc_tot(10,10,10)) == 'You are awarded provincial colours!'
    except:
        print("Error on assertion") 
    finally:
        print("Going to next")
           
    try:
        assert obtain_award(calc_tot(33,33,34)) == 'You are awarded provincial colours!'
    except:
        print("Error on assertion") 
    finally:
        print("Going to next")

    try:
        assert obtain_award(calc_tot(30,40,34)) == 'You are awarded half colours!'
    except:
        print("Error on assertion") 
    finally:
        print("Going to next")

    try:
        assert obtain_award(calc_tot(30,40,40)) == 'You will be placed on the provincial scroll!'
    except:
        print("Error on assertion") 
    finally:
        print("Going to next")

    try:
        assert obtain_award(calc_tot(45,45,45)) == 'Bad luck, you never received an award!'
    except:
        print("Error on assertion") 
    finally:
        print("Exiting")

    
if __name__ == '__main__':
    test()