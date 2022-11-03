import matplotlib.pyplot as plt


def Drawparabola(a, h, k):  # 开口系数a,顶点坐标(h,k)
    xs = []
    ys = []
    x = h
    y = k
    p = y + 0.5 - a * (x + 1 - h) - k
    while 2 * a * (x + 1 - h) < 1:  # 以k = -1为分界
        xs.append(x)
        ys.append(y)
        if p < 0:
            p += 1 - a - 2 * a * (x + 1 - h)
            x += 1
            y += 1
        else:
            p += -a - 2 * a * (x + 1 - h)
            x += 1
    p = y + 1 - a * (x + 0.5 - h) - k
    while y < 40:
        xs.append(x)
        ys.append(y)
        if p > 0:
            x += 1
            y += 1
            p += 1 - a - 2 * a * (x + 0.5 - h)
        else:
            y += 1
            p += 1
    plt.show()
    plt.axis('equal')
    # plt.grid(True)
    plt.axvline(x=0, linewidth=1, color='k')  # v x轴
    plt.axhline(y=0, linewidth=1, color='k')  # h y轴
    plt.axis([-50, 50, -50, 50], 'equal')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.axis('equal')
    for i in range(0, len(xs)):
        if i == 0:
            plt.scatter(xs[i], ys[i], color='k', s=1)
            plt.pause(0.1)
        else:
            plt.scatter(xs[i], ys[i], color='k', s=1)
            plt.scatter(2 * h - xs[i], ys[i], color='k', s=1)
            plt.pause(0.1)
            plt.draw()
    plt.show()


#DraweParabola(0.2, 1, 1)
