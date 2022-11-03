'''
中点分割裁剪算法
'''

import matplotlib.pyplot as plt
import numpy as np
import cmath

LEFT = 1  # 0001 左
RIGHT = 2  # 0010 右
BOTTOM = 4  # 0100 下
TOP = 8  # 1000 上

XL = 40
XR = 100
YB = 40
YT = 100


def bction():
    def DDALine(image, x0, y0, x1, y1, color):
        dx = x1 - x0
        dy = y1 - y0

        if dx != 0:
            k = dy / dx
        else:
            for i in range(y0, y0 + dy + 1):
                image[i][x0] = color
            else:
                for i in range(y1, y1 - dy + 1):
                    image[i][x0] = color
            return
        if k >= 0:
            if abs(k) < 1:
                y = y0
                xmin = x0
                xmax = x1
                for i in range(xmin, xmax + 1):
                    image[int(y + 0.5)][i] = color
                    y = y + k
            else:
                x = x0
                if y0 < y1:
                    ymin = y0
                    ymax = y1
                else:
                    ymin = y1
                    ymax = y0
                for i in range(ymin, ymax + 1):
                    image[i][int(x + 0.5)] = color
                    x = x + 1.0 / k
        elif k < 0:  # k<0
            if k > -1:
                y = y0
                xmin = x0
                xmax = x1
                for i in range(xmin, xmax + 1):
                    image[int(y + 0.5)][i] = color
                    y = y + k
            else:
                x = x1
                if y0 < y1:
                    ymin = y0
                    ymax = y1
                else:
                    ymin = y1
                    ymax = y0
                for i in range(ymin, ymax + 1):
                    image[i][int(x + 0.5)] = color
                    x = x + 1.0 / k

    def draw(image, graph, color):
        l = len(graph)
        for i in range(l):
            [x0, y0] = graph[i]
            [x1, y1] = graph[(i + 1 + l) % l]
            if x0 > x1:
                temp = x1
                x1 = x0
                x0 = temp
                temp = y1
                y1 = y0
                y0 = temp

            DDALine(image, x0, y0, x1, y1, color)

    def encode(x, y):
        c = 0
        if (x < XL):
            c = c | LEFT
        if (x > XR):
            c = c | RIGHT
        if (y < YB):
            c = c | BOTTOM
        if (y > YT):
            c = c | TOP
        return c

    def MidClip(polygon, image):
        image = image

        l = len(polygon)
        for i in range(l):
            [x1, y1] = polygon[i]
            [x2, y2] = polygon[(i + 1 + l) % l]

            print(x1)
            print(y1)
            print(x2)
            print(y2)
            print("\n")
            flag = 0
            code1 = encode(x1, y1)  # p1
            code2 = encode(x2, y2)  # p2
            print(code1)
            print(code2)
            if (code1 == 0 and code2 == 0):  # 同时为0,在窗口内部，不用裁剪
                flag = 2
            elif (code1 & code2 != 0):  # 在窗口外部
                flag = 1
            else:
                ff = 0
                # s=2                           #避免计算
                if (code2 == 0):
                    [xa, ya] = [x2, y2]  # 检测p2是否在窗口内部，是则为所求点
                    ff = 1

                while ((abs(x1 - x2) > 1 or abs(y1 - y2) > 1) and ff == 0):  # 从p1出发
                    # xmid=(int)((x1+x2)/2)
                    # ymid=(int)((y1+y2)/2)
                    print(x1)
                    print(x2)
                    xmid = (x1 + x2) / 2
                    ymid = (y1 + y2) / 2
                    codem = encode(xmid, ymid)
                    print(xmid)
                    print(ymid)
                    print(codem)

                    if (((ymid == YT) and (XL <= xmid <= XR)) or ((ymid == YB) and (XL <= xmid <= XR))):
                        [xa, ya] = [xmid, ymid]
                        break
                    elif (codem == 0):  # 若中点在窗口内部
                        x1 = xmid
                        y1 = ymid
                    elif (codem & code2 != 0):  # 中点和p2在同一侧外面
                        x2 = xmid
                        y2 = ymid
                    elif (codem & code1 != 0):
                        x1 = xmid
                        y1 = ymid
                    # s=(float)(cmath.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))
                    # s=2
                    # exit(0)
                if (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1):
                    [xa, ya] = [x2, y2]

                [x1, y1] = polygon[i]
                [x2, y2] = polygon[(i + 1 + l) % l]
                fff = 0
                if (code1 == 0):
                    [xb, yb] = [x1, y1]  # 检测p1是否在窗口内部，是则为所求点
                    fff = 1
                while ((abs(x1 - x2) > 1 or abs(y1 - y2) > 1) and fff == 0):  # 从p2出发
                    # xmid = (int)((x1 + x2) / 2)
                    # ymid = (int)((y1 + y2) / 2)
                    xmid = (x1 + x2) / 2
                    ymid = (y1 + y2) / 2
                    codem = encode(xmid, ymid)
                    if (((ymid == YT) and (XL <= xmid <= XR)) or ((ymid == YB) and (XL <= xmid <= XR))):
                        [xa, ya] = [xmid, ymid]
                        break
                    elif (codem == 0):  # 若中点在窗口内部
                        x2 = xmid
                        y2 = ymid
                    elif (codem & code1 != 0):  # 中点和p2在同一侧外面
                        x1 = xmid
                        y1 = ymid
                    elif (codem & code2 != 0):
                        x2 = xmid
                        y2 = ymid
                        # s = (float)(cmath.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
                if (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1):
                    [xb, yb] = [x1, y1]
            if (flag == 1):
                pass
            elif (flag == 2):
                if (x1 > x2):
                    temp = x2
                    x2 = x1
                    x1 = temp
                    temp = y2
                    y2 = y1
                    y1 = temp
                DDALine(image, x1, y1, x2, y2, False)
            else:
                if (xa > xb):
                    temp = xb
                    xb = xa
                    xa = temp
                    temp = yb
                    yb = ya
                    ya = temp
                DDALine(image, (int)(xa + 0.5), (int)(ya + 0.5),
                        (int)(xb + 0.5), (int)(yb + 0.5), False)

    image = np.ones([150, 150])
    plt.xlim(0, 150)
    plt.ylim(0, 150)

    window = [
        [40, 40],
        [40, 100],
        [100, 100],
        [100, 40]
    ]

    polygon = [
        [20, 20],
        [120, 20],
        [70, 100],
        [50, 80],
        [30, 120],
        [20, 50],
        [50, 50]
    ]
    draw(image, window, False)

    # draw(image,polygon,False)

    MidClip(polygon, image)

    plt.imshow(image, plt.cm.gray)
    plt.show()
