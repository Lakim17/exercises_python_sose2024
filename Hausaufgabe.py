
def spar_funktion(AK,SR,i,lz):
    kapital=AK
    gesamt_kaptial = []
    for k in range(1,lz+1):
        Kapital+=kapital*(1+i)+SR
        gesamt_kaptial.append(AK)
    return gesamt_kaptial

print(spar_funktion(AK=10000, SR=1000, i=0.01, lz=10))

        
        