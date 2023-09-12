#!/usr/bin/env python3

def function(x:int):
    if x ==1:
        i = True
    else:
        i = False
        print("Going ahead") # negates the loop
    
    while i == True:
        # an infinite loop with no method of escape if i is True, otherwise it is passed over if i is False
        print(f"Too {i}")
              
# this code may never be reached if x is set to 1:logic error?
    long_str = "this is not so far fetched that Jamaica could lose her husband just after she had given a child"
    long_array = long_str.split(" ")
    
    for count, item in enumerate(long_array):
        print(f"{count}::{item}") #compilation error::syntax error "missing the right parenthesis to print"
        
if __name__ == "__main__":
    function(0)
