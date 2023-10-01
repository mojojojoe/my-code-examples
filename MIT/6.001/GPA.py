def obtain_class_scores():
    n = int(input("How many classes did you take? "))
    D = []
    i = 0
    while i < n:
        cod, grd = input("What was the course code? "), int(input("What was the course grade? "))
        D.append((cod, grd))
        i += 1
    return D

def find_avg_gpa(D):
    G = []
    for i in D:
        cod, grd = i
        if grd >= 93:
            GPA = 4.0
        elif grd >= 90 and grd < 93:
            GPA = 3.7
        elif grd >= 87 and grd < 90:
            GPA = 3.3
        elif grd >= 83 and grd < 87:
            GPA = 3.0
        elif grd >= 80 and grd < 83:
            GPA = 2.7
        elif grd >= 77 and grd < 80:
            GPA = 2.3
        elif grd >= 73 and grd < 77:
            GPA = 2.0
        elif grd >= 70 and grd < 73:
            GPA = 1.7
        elif grd >= 67 and grd < 70:
            GPA = 1.3
        elif grd >= 65 and grd < 67:
            GPA = 1.0
        else:
            GPA = 0.0
        G.append((cod, GPA))
    return G

def main():
    g = 0
    c = ''
    n = 0
    gt = 0

    G = find_avg_gpa(obtain_class_scores())

    for t in G:
        c, g = t
        gt += g
        n += 1

    print("Avg GPA: ", gt/n)

if __name__ == '__main__':
    main()
