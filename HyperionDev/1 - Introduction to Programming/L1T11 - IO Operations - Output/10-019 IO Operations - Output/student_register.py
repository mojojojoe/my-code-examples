#!/usr/bin/env python3.11

def register_students():
    num_students = int (input ("How many students are going to register?")) 
    count = 0
    id = []
    while (count < num_students):
        id.append(int (input ("Please enter the next student number: ")))
        count += 1
    
    with open ('reg_form.txt', 'w+') as of:
        for num in id:
            of.write (f"{str(num)}\t\t................\n")
        

if __name__ == "__main__":
    register_students ()
