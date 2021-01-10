from prog import Cluster
import random
import matplotlib.pyplot as plt
size = 4
trans = 1
# Тест на случайных точках
print('test1')
xy_1 = []
xy_2 = []
x_1 = []
y_1 = []
x_2 = []
y_2 = []
for i in range(300):
    x_1.append(random.randint(-100,100))
    x_2.append(random.randint(-100,100))
    y_1.append(random.randint(-100,100))
    y_2.append(random.randint(-100, 100))
    xy_1.append([x_1[i],y_1[i]])
    xy_2.append([x_2[i],y_2[i]])
xy = xy_1 + xy_2
cls = [xy_1,xy_2]
Cluster.clusterring(xy, cls, len(cls))

# Тестируем на простых квадратах
print('test2')
c1 = []
c2 = []
c3 = []
for i in range(3):
    for j in range(3):
        c1.append([2+i,2+j])
        c2.append([6 + i, 6 + j])
        c3.append([8 + i, 2 + j])
xy = c1 + c2 + c3
cls = [c1,c2,c3]
Cluster.clusterring(xy, cls, len(cls))


# Ромб, треугольник, квадрат
print('test3')
rhombus = []
for i in range(500):
    rhombus.append([i, 1500 + i])
    rhombus.append([500 + i, 2000 - i])
    rhombus.append([1 + i, 1499 - i])
    rhombus.append([501 + i, 1001 + i])
square = []
for i in range(1000):
        square.append([1002 + i,1001])
        square.append([1001, 1001 + i])
        square.append([2001, 1002 + i])
        square.append([1001 + i, 2001])
triangle = []
for i in range(2001):
    triangle.append([i,0])
    if i <= 1000:
        triangle.append([i,i])
    else:
        triangle.append([i, 2000 - i])
xy = rhombus + square + triangle
cls = [rhombus, square, triangle]
Cluster.clusterring(xy, cls, len(cls))

# Окружность с точкой внутри
print('test4')
circle = []
for i in range(10000*1 + 1):
    a = i/10000
    for j in range(10000*1, 10000*2 + 1):
        b = j/10000
        if round(a**2 + b**2, 3) == 2**2:
            circle.append([a, b])
            circle.append([-a, b])
            circle.append([a, -b])
            circle.append([-a, -b])
            circle.append([b, a])
            circle.append([-b, a])
            circle.append([b, -a])
            circle.append([-b, -a])
point = [[0,0]]
xy = circle + point
cls = [circle, point]
Cluster.clusterring(xy,cls,len(cls))

# Блоки точек и диагональ
print('test5')
tr1 = []
tr2 = []
d = [[0, 0]]
for i in range(1000):
    for j in range(1000):
        if (i > 1 and j >= 1) or (i >= 1 and j > 1):
            tr1.append([i, j])
            tr2.append([-i, -j])
        if (i > 0):
            d.append([-i, i])
            d.append([i, -i])
xy = tr1 + tr2 + d
cls = [tr1,tr2,d]
Cluster.clusterring(xy, cls, len(cls))