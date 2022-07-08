#формула Герона s=корень из(p(p-a)(p-b)(p-c)
#где p=(a+b+c)/2

side_a = input("Введите длину стороны a: ")
a = int(side_a)
side_b = input("Введите длину стороны b: ")
b = int(side_b)
side_c = input("Введите длину стороны c: ")
c = int(side_c)
print("Стороны треугольника: a=",a,"см")
print("Сторона треугольника b=",b,"см")
print("Сторона треугольника c=",c,"см")
p_triangel=((a+b+c)/2)
import math
s_triangel = ((p_triangel)*(p_triangel-a)*(p_triangel-b)*(p_triangel-c))
sqrt = math.sqrt(s_triangel)
print("Площадь треугольника " ,str(sqrt))
