import matplotlib.pyplot as plt

s_n =  []
a = 1
r = 0.5
n = 10
Summe = 0
for k in range(0,n):
    Summe += a * r ** k
    s_n.append(Summe)

print(s_n)


plt.plot(s_n)
