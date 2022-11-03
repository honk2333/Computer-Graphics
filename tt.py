from functools import cmp_to_key as ctk
import random

class point(object):
    def __init__(self, *arg):
        self.x = int()
        self.y = int()
        if len(arg) == 1:
            if isinstance(arg[0],point):
                self.x = arg[0].x
                self.y = arg[0].y
            else:
                self.x = int(arg[0][0])
                self.y = int(arg[0][1])
        elif len(arg) == 2:
            self.x = int(arg[0])
            self.y = int(arg[1])

    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return point(self.x-other.x, self.y-other.y)

    def __xor__(self, other):
        return self.x*other.y - self.y*other.x

    def __truediv__(self, other):
        return point(self.x/other, self.y/other)

    def __mul__(self, other):
        return self.x*other.x+self.y*other.y

    def __str__(self):
        return '(%.2f,%.2f)' % (self.x, self.y)

    def __repr__(self):
        return '(%.2f,%.2f)' % (self.x, self.y)

    def len(self):
        return (self.x*self.x+self.y*self.y)**0.5

    def __cmp__(self, other):
        return self.y == other.y and self.x == other.x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x        

    def __lt__(self, other):
        return self.x < other.x if self.y == other.y else self.y < other.y


def degree(sel, other):
    return (sel ^ other)/(other.len())


def cp(sel):
    if sel == min_:
        return 0
    return degree(point(1, 0), sel-min_)


def cp1(sel, other):
    global min_
    if sel == min_:
        return True
    tmp = (sel-min_) ^ (other-min_)
    if tmp > 0:
        return True
    elif tmp == 0 and (sel-min_).len() < (sel-min_).len():
        return True
    return False

def QSort(sth):
    if len(sth)==0 or len(sth)==1:
        return sth

    t=sth[random.randint(0,len(sth)-1)]
    m=[x for x in sth if cp1(x,t)]
    n=[x for x in sth if not cp1(x,t)]
    return QSort(m)+QSort(n)

min_ = point(1000000, 1000000)

def solve(n,m):
    # print(min_)
    global min_
    for i in range(n):
        m[i] = point(m[i])
        if m[i] < min_:
            min_ = m[i]
    stk = [min_]
    m=QSort(m)
    pre = None
    for i in m:
        if i == min_:
            continue
        if len(stk) > 1:
            while len(stk) > 1 and stk[-1]-stk[-2] ^ (i-stk[-1]) <= 0:
                stk.pop()
            stk.append(i)
        else:
            stk.append(i)

    ans = 0
    pre = stk[-1]
    for i in stk:
        ans += (i-pre).len()
        pre = i

    return stk

if __name__ == '__main__':
    print(type(point()))