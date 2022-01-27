import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('classic_run3.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

plt.plot(x, y, color='g', linestyle='dashed',
         marker='o', label="LoadTime Data")

plt.xticks(rotation=25)
plt.xlabel('Frontend Performance')
plt.ylabel('BackEnd Performance')
plt.title('Load Time', fontsize=15)
plt.grid()
plt.legend()
plt.show()