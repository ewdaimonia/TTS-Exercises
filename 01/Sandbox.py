# https://docs.python.org/3/faq/programming.html#why-did-changing-list-y-also-change-list-x
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
print("Using assignment (assigning same location in memory)")
x = [1, 2, 3]
y = x
x.append(5)
x = str(x)
print(x)
print(y)

print("Using copy method")
x = [1, 2, 3]
y = x.copy()
x.append(5)
x = str(x)
print(x)
print(y)

print("Using slice method")
x = [1, 2, 3]
y = x[:]
x.append(5)
x = str(x)
print(x)
print(y)
