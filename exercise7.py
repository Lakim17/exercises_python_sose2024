
def buchstaben_zählen(x):
    s = 0
    for k in x:
        if k.isalpha():
            s += 1
            print(s)
    
buchstaben_zählen("Hallo Berlin")
