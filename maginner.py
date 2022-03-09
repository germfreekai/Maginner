def maginner(str):
    print(str)

def concat(c):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    for x in c:
        line1 = line1 + x[0]
        line2 = line2 + x[1]
        line3 = line3 + x[2]
        line4 = line4 + x[3]
        line5 = line5 + x[4]
        line6 = line6 + x[5]

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)

def A(): 
    A = []   
    A.append(" _____ ")  #0
    A.append("|     |") #1
    A.append("|  ▄  |") #2 
    A.append("|     |") #3
    A.append("|  |  |") #4
    A.append("|__|__|") #5 --> 7 de largo

    return A

def B():
    B = []
    B.append(" _____ ")
    B.append("|     |")
    B.append("|   ▄ |")
    B.append("|   __|")
    B.append("|   ▄ |")
    B.append("|_____|")

    return B

def C():
    C = []
    C.append(" _____ ")
    C.append("|   __|")
    C.append("|  |   ")
    C.append("|  |   ")
    C.append("|  |__ ")
    C.append("|_____|")

    return C
                 
a = A()
b = B()
c = C()

msg = []
msg.append(a)
msg.append(b)
msg.append(c)

#print(len(c))
#print(c)
concat(msg)
