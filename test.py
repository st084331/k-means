from prog import Cluster
import random
# Тест на случайных точках
print('test1')
xy = []
for i in range(1000):
    xy.append([random.randint(-100,100), random.randint(-100,100)])
Cluster.clusterring(xy, [], random.randint(2,20))

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
Cluster.clusterring(xy, cls, 3)

# Ромб, треугольник, квадрат
print('test3')
rhombus = [[0,3],[1,2],[2,3],[1,4]]
square = []
for i in range(3):
    for j in range(3):
        if i == 1:
            square.append([3+j, 2+i])
            j+=1
        else:
            square.append([3+j, 2+i])
triangle = [[1,1], [3,1], [2,2]]
for i in range(5):
    triangle.append([i,0])
xy = rhombus + square + triangle
cls = [rhombus, square, triangle]
Cluster.clusterring(xy, cls, 3)

# Окружность с точкой внутри
print('test4')
circle = [[5,0],[-5,0],[0,5],[0,-5],[3,4],[-3,-4],[4,3],[-4,-3]]
point = [[0,0]]
xy = circle + point
cls = [circle, point]
Cluster.clusterring(xy,cls,2)

# "Маленькие" данные
print('test5')
tr1 = []
tr2 = []
d = []
for i in range(10):
    d.append([0, 0])
    d.append([1, -1])
    d.append([-1, 1])
    tr1.append([1,1])
    tr1.append([1,0])
    tr1.append([0,1])
    tr2.append([-1,-1])
    tr2.append([-1,0])
    tr2.append([0,-1])
xy = tr1 + tr2 + d
cls = [tr1,tr2,d]
Cluster.clusterring(xy, cls, 3)