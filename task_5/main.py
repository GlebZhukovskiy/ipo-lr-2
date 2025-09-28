import math

class_1 = int(input("Введите количество человек в первом классе"))
class_2 = int(input("Введите количество человек во втором классе"))
class_3 = int(input("Введите количество человек в третьем  классе"))

all = math.ceil((class_1 + class_2 + class_3) / 2)
print ("Нужно закупить ",all , "парт")