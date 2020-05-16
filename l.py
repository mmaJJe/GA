import matplotlib.pyplot as plt
import tsp
import csv

dots = []
f = open('building.csv','r')
rdr = csv.reader(f)
dots.append((0,0))
for line in rdr:
    x = int(line[0])
    y = int(line[1])
    dots.append((x,y))
dots.append((0,0))
f.close()
# t = tsp.tsp(dots)
# print("거리는 : "+ str(t[0]))
# li =
# or_li = 
# for dot in li:
#    or_li.append(dot[0])
# or_li
order_li = 0, 2, 27, 95, 46, 58, 72, 80, 18, 47, 84, 94, 54, 5, 12, 32, 22, 29, 59, 99, 8, 86, 67, 83, 6, 36, 38, 45, 78, 85, 48, 34, 26, 19, 61, 69, 70, 4, 15, 96, 60, 40, 42, 33, 77, 43, 16, 50, 73, 75, 81, 76, 13, 14, 20, 23, 35, 90, 92, 97, 9, 91, 31, 68, 56, 82, 87, 74, 71, 44, 88, 37, 52, 98, 3, 63, 17, 21, 51, 62, 66, 1, 53, 55, 11, 7, 25, 79, 39, 64, 24, 10, 57, 93, 28, 41, 30, 65, 49, 89, 100
print(len(order_li))
y_li = []
x_li = []
for order in order_li:
    x_li.append(dots[order][0])
    y_li.append(dots[order][1])


plt.figure() # marker 인자를 같이 적는다.
plt.plot(x_li, y_li, marker='o') 
plt.show()

