from math import pi, exp




def teilbar(x,y):
    if y == 0:
        print("es ist nicht möglich durch 0 zu teilen!")
    else:
        if x % y == 0:
            print(str(x) + " ist durch " + str(y) + " teilbar")
        else:
            print(str(x)+ " ist nicht durch " + str(y) + " teilbar")
        if x == y:
            print(str(x) + " und " + str(y) + " sind gleich")
        print("Wenn man " + str(x) + " durch " + str(y) + " teilt, kommt " +  str(x/y) + " raus")


teilbar(pi,pi)

def division(x,y):
    if y == 0:
        print("es ist nicht möglich durch 0 zu teilen!")
    elif x == y:
        print(str(x) + " und " + str(y) + " sind gleich")
    elif x % y == 0:
        print(str(x) + " ist durch " + str(y) + " teilbar")
    else:
        print(str(x)+ " ist nicht durch " + str(y) + " teilbar")

    if not y == 0: 
        print("Wenn man " + str(x) + " durch " + str(y) + " teilt, kommt " +  str(x/y) + " raus")
    
division(3,0)