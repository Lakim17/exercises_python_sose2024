import numpy as np
import pandas as pd

#1

index = ["Berlin", "Madrid", "Rom"]
bevölkerung  = pd.Series(data = [3.6, 3.3, 2.8], index = index)
fläche = pd.Series(data = [892, 604, 1285], index = index)
land = pd.Series(data = ["Deutschland", "Spanien", "Italien"], index = index)
sprache = pd.Series(data = ["deutsch", "spanisch", None], index = index)

my_dict = {'Bevölkerung': bevölkerung,
           'Fläche': fläche,
           'Land': land,
           'Sprache': sprache}

df = pd.DataFrame(my_dict)

#2


