def steigung_funktion(Liste):
    x1 = Liste[0]
    y1 = Liste[1]
    x2 = Liste[2]
    y2 = Liste[3]
    if x1 == x2:
        print("Die Steigung ist nicht definiert")
    else:
        print((y2-y1)/(x2-x1))
        