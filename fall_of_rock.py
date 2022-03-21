from diffur_methods import yn1, yn2
import matplotlib.pyplot as plt


k = 0.001


def fy2(time, sp, co):
    a = -9.8
    return a


def fy1(time, sp, co):
    a = sp
    return a


def fx1(time, sp, co):
    a = sp
    return a


def fx2(time, sp, co):
    a = 0
    return a


def f2y2(time, ys, yc, xs, xc):
    a = -9.8 + k * (xs**2 + ys**2) * (yc / ((yc**2 + xc**2)**0.5))
    if a >= 0:
        a = 0
    return a


def f2y1(time, ys, yc, xs, xc):
    a = ys
    return a


def f2x2(time, ys, yc, xs, xc):
    a = -k * (xs**2 + ys**2) * (xc / ((yc**2 + xc**2)**0.5))
    return a


def f2x1(time, ys, yc, xs, xc):
    if xs >= 0:
        a = xs
    else:
        a = 0
    return a


x1 = 10
x = 0
y1 = 0
y = 100
dt = 0.001
t = 0
y2 = y
x2 = x
x21 = x1
y21 = y1

graphx = [x]
graphy = [y]
graphx2 = [x]
graphy2 = [y]

while y > 0:
    b = yn1(fy2, fy1, t, y, y1, dt)
    y = b[1]
    y1 = b[0]
    c = yn1(fx2, fx1, t, x, x1, dt)
    x = c[1]
    x1 = c[0]
    b2 = yn2(f2y2, f2y1, f2x2, f2x1, t, y2, y21, x2, x21, dt)
    y2 = b2[1]
    y21 = b2[0]
    x21 = b2[2]
    x2 = b2[3]
    t = t + dt
    graphx.append(x)
    graphy.append(y)
    graphx2.append(x2)
    graphy2.append(y2)

plt.plot(graphx, graphy)
plt.plot(graphx2, graphy2)
print(x, y, x2, y2)
plt.show()
