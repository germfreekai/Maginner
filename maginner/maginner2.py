def maginner(str):

    str = str.lower()
    msg = []

    keys = {'a' : A(), 'b' : B(), 'c' : C(), 'd' : D(), 'e' : E(), 'f' : F(),
            'g' : G(), 'h' : H(), 'i' : I(), 'j' : J(), 'k' : K(), 'l' : L(),
            'm' : M(), 'n' : N(), 'o' : O(), 'p' : P(), 'q' : Q(), 'r' : R(),
            's' : S(), 't' : T(), 'u' : U(), 'v' : V(), 'w' : W(), 'x' : X(),
            'y' : Y(), 'z' : Z(), ' ' : blank_space(), '.' : dot()}

    for letter in str: 
        if letter in keys: 
            msg.append(keys[letter])
        else: 
            return 0

    concat(msg)
    
    return 1

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

def D():
    D = []
    D.append(" _ ____ ")
    D.append("| |    |")
    D.append("|      |")
    D.append("|    ▄ |")
    D.append("|      |")
    D.append("|_|____|")

    return D   

def E():
    E = []
    E.append(" ______ ")
    E.append("|   ___|")
    E.append("|  |___ ")
    E.append("|   ___|")
    E.append("|  |___ ")
    E.append("|______|")

    return E   

def F():
    F = []
    F.append(" ______ ")
    F.append("|   ___|")
    F.append("|  |___ ")
    F.append("|   ___|")
    F.append("|  |    ")
    F.append("|__|    ")

    return F

def G():
    G = []
    G.append(" ______ ")
    G.append("|  ____|")
    G.append("| | ___ ")
    G.append("| ||_  |")
    G.append("| |__| |")
    G.append("|______|")

    return G

def H():
    H = []
    H.append(" _    _ ")
    H.append("| |  | |")
    H.append("| |__| |")
    H.append("|  __  |")
    H.append("| |  | |")
    H.append("|_|  |_|")

    return H

def I():
    I = []
    I.append(" ______ ")
    I.append("|__  __|")
    I.append("   ||   ")
    I.append("   ||   ")
    I.append(" __||__ ")
    I.append("|______|")

    return I

def J():
    J = []
    J.append(" ______ ")
    J.append("|__  __|")
    J.append("   | |  ")
    J.append("   | |  ")
    J.append(" __| |  ")
    J.append("|____|  ")

    return J

def K():
    K = []
    K.append(" _   __")
    K.append("| | / /")
    K.append("| |/ / ")
    K.append("|   /  ")
    K.append("| |\\ \\ ")
    K.append("|_| \\_\\")

    return K

def L():
    L = []
    L.append(" _      ")
    L.append("| |     ")
    L.append("| |     ")
    L.append("| |     ")
    L.append("| |____ ")
    L.append("|______|")

    return L

def M():
    M = []
    M.append(" __  __ ")
    M.append("|  \\/  |")
    M.append("|      |")
    M.append("| |\\/| |")
    M.append("| |  | |")
    M.append("|_|  |_|")

    return M

def N():
    N = []
    N.append(" _    _ ")
    N.append("| \\  | |")
    N.append("|  \\ | |")
    N.append("|   \\| |")
    N.append("| |\\   |")
    N.append("|_| \\__|")

    return N

def O():
    O = []
    O.append(" _______ ")
    O.append("|       |")
    O.append("|       |")
    O.append("|   ▄   |")
    O.append("|       |")
    O.append("|_______|")

    return O

def P():
    P = []
    P.append(" ______ ")
    P.append("|      |")
    P.append("|    ▄ |")
    P.append("|  ____|")
    P.append("| |     ")
    P.append("|_|     ")

    return P

def Q():
    Q = []
    Q.append(" ______ ")
    Q.append("|      |")
    Q.append("|      |")
    Q.append("|   ▄  |")
    Q.append("|      |")
    Q.append("|___\\_\\|")

    return Q

def R():
    R = []
    R.append(" ______ ")
    R.append("|      |")
    R.append("|    ▄ |")
    R.append("|    __|")
    R.append("| |\\ \\  ")
    R.append("|_| \\_\\ ")

    return R

def S():
    S = []
    S.append(" ______ ")
    S.append("|   ___|")
    S.append("|  |___ ")
    S.append("|___   |")
    S.append(" ___|  |")
    S.append("|______|")

    return S

def T():
    T = []
    T.append(" ______ ")
    T.append("|__  __|")
    T.append("  |  |  ")
    T.append("  |  |  ")
    T.append("  |  |  ")
    T.append("  |__|  ")

    return T

def U():
    U = []
    U.append(" __   __ ")
    U.append("|  | |  |")
    U.append("|  | |  |")
    U.append("|  | |  |")
    U.append("|  |_|  |")
    U.append("|_______|")

    return U

def V():
    V = []
    V.append("        ")
    V.append("|\\    /|")
    V.append("| \\  / |")
    V.append("|  \\/  |")
    V.append(" \\    / ")
    V.append("  \\__/  ")

    return V

def W():
    W = []
    W.append("        ")
    W.append("|\\    /|")
    W.append("| \\/\\/ |")
    W.append("|      |")
    W.append("|      |")
    W.append(" \\_/\\_/ ")

    return W

def X():
    X = []
    X.append(" _    _ ")
    X.append("\\ \\  / /")
    X.append(" \\ \\/ / ")
    X.append("  /  \\  ")
    X.append(" / /\\ \\ ")
    X.append("/_/  \\_\\")

    return X

def Y():
    Y = []
    Y.append(" _    _ ")
    Y.append("\\ \\  / /")
    Y.append(" \\ \\/ / ")
    Y.append("  \\  /  ")
    Y.append("  / /   ")
    Y.append(" /_/    ")

    return Y

def Z():
    Z = []
    Z.append(" ______ ")
    Z.append("|__    /")
    Z.append("   /  / ")
    Z.append("  /  /  ")
    Z.append(" /  /__ ")
    Z.append("|______|")

    return Z

def blank_space():
    BlankSpace = []
    BlankSpace.append("  ")
    BlankSpace.append("  ")
    BlankSpace.append("  ")
    BlankSpace.append("  ")
    BlankSpace.append("  ")
    BlankSpace.append("  ")

    return BlankSpace

def dot():
    Dot = []
    Dot.append(" ")
    Dot.append(" ")
    Dot.append(" ")
    Dot.append(" ")
    Dot.append(" ")
    Dot.append("▄")

    return Dot



maginner("lopkjhyutredcvbx")