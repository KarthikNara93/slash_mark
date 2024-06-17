from matplotlib import pyplot as k
# Create a simple plot
x = [1, 2, 13, 14, 25]
y = [1, 4, 9, 16, 25]

k.plot(x, y)
k.xlabel('X-axis')
k.ylabel('Y-axis')
xx=[22,33,44,55,6,6,88]
yy=sorted([77,66,98,66,99,33,2])
k.plot(xx, yy)
k.title('Simple Plot')
k.legend(['a','b'])
k.show()
