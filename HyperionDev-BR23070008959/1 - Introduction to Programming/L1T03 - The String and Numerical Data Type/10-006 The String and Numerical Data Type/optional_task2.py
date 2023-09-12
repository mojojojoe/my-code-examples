#!/usr/bin/env python3

def task2():
    string_fav = input("Please type in the name of your favourite restaurant: ")
    int_fav = int(input("Please type in your favourite number: "))
    
    print(f"\n{string_fav}")
    print(f"\n{int_fav}\n")
    try:
        int(string_fav)
    except: 
        print("Something went wrong with the casting!")
    finally:
        return 0
    
               
if __name__ == '__main__':
    task2()