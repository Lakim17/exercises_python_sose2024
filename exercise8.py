def vokon_zählen(x):
    vokal = "aeiouäöü"
    konso = "qwrtzplkjhgfdsyxcvbnmß"
    
    x_lower = x.lower()
    
    voza = [i for i in x_lower if i in vokal]
    koza = [k for k in x_lower if k in konso]
    
    print(f"Es gibt {len(voza)} Vokale und {len(koza)} Konsonanten.")

vokon_zählen("Hallo, Berlin%%%!")

def vokon_zähler(wort):
    vokalen = "aeiou"
    wort_lower = wort.lower()
    
    buchstaben = [i for i in wort_lower if i.isalpha()]
    Vokalen = [k for k in wort_lower if k in vokalen]
    
    print(f"""Es gibt im Wort "{wort}" {len(Vokalen)} Vokale und {len(buchstaben) - len(Vokalen)} Konsonanten!!!!!!!!""")
          
vokon_zähler("HallO, Berlin%%%!")