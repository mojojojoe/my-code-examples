#!/usr/bin/env python3

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def extract_from(file):
    name = ""
    date = ""
    with open(file) as fh:
        for line in fh:
            stra = line.split(" ")
            name += (stra[0] + " " + stra[1] + "\n")
            date += (stra[2] + " " + stra[3] + " " + stra[4])
    return name, date

if __name__ == "__main__":
    name, date = extract_from('DOB.txt')
    print(style.BOLD + "Name" + style.END)
    print(name)
    print(style.BOLD + "Date" + style.END)
    print(date)    