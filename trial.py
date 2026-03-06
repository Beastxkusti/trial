import matplotlib.pyplot as plt

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

lb = float(input('batas bawah = '))
ub = float(input('batas atas = '))

axis_x = []
axis_y = []

x = lb
while x <= ub:
    axis_x.append(x)
    
    y = a*x**2 + b*x + c
    axis_y.append(y)
    
    x += 0.1

plt.plot(axis_x, axis_y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(f"Grafik f(x) = {a}x² + {b}x + {c}")
plt.show()