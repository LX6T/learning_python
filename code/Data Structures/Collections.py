# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaaabbbbccc"
mycounter = Counter(a)  # dictionary with character counts
print(mycounter)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(1))
print(mycounter.most_common(1)[0])
print(mycounter.most_common(1)[0][1])
print(list(mycounter.elements()))

print("")

from collections import namedtuple

Point = namedtuple('Point', 'x,y')  # fancy tuple
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

print("")

from collections import OrderedDict

ordereddict = OrderedDict()  # dictionary remembers item creation order
ordereddict['a'] = 1
ordereddict['b'] = 2
ordereddict['c'] = 3
ordereddict['d'] = 4
print(ordereddict)

print("")

from collections import defaultdict

d = defaultdict(int)  # dictionary with default values
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['b'])
print(d['c'])

print("")

from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4, 5, 6])
print(d)
d.extendleft([3, 2, 1])
print(d)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-3)
print(d)
