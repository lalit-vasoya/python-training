from collections import Counter,defaultdict,OrderedDict,deque,ChainMap,namedtuple

l=[1,2,3,4,4,5,2,3]

c=Counter(l)

for i in c.elements():
	print(i)



for i in c.most_common():
	print(i[0],":::",i[1])


d=defaultdict(lambda:"default value")
d["a"]=2
d["b"]=1

print(d[0])


a=OrderedDict({"a":10,"b":20,"c":30,"d":40})

for i,j in a.items():
	print(i,j)

q=deque(["a","b","c"])
print(q)
q.append("d")
q.appendleft(1)

print(q)


c=ChainMap({"a":2,"b":3},{"a":6,"c":9},{"d":7})
print(c)

print(c["a"])

print("Keys And Value:")
print(list(c.keys()))
print(list(c.values()))

print(c.maps)


s=namedtuple('student',['name','age','marks'])

print(s)
a=s("lalit",18,94)
print(a)

b=s._make(["kalpesh",19,75])
print(b)

		

