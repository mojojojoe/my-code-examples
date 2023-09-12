#!/usr/bin/env python3

def replace ():
    fox = "the!quick!brown!fox!jumps!over!the!lazy!dog"
    print (fox.replace("!"," "))
    print (fox.upper().replace("!"," "))
    print (fox.replace("!"," ") [::-1])
    

if __name__ == '__main__':
    replace()
