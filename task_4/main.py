import math

x = int(input("Введите x "))
y = int(input("Введите y "))
#(pow(math.exp , abs(x - y)))
u = ((pow(8 + pow(abs(x - y), 2) + 1, 1/3)) / (pow(x, 2) + pow(y, 2) + 2)) - (math.e ** abs(x - y))
print(u)