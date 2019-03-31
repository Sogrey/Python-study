def howlong(frist, *other):
    print(1 + len(other))


howlong("hello", 1, '2', 3.2)

var1 = '123'


def func():
    global var1
    var1 = 456
    print(var1)


func()
print(var1)

list = [1, 2, 3]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) #StopIteration

for i in range(10, 20, 2):
    print(i)


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(10, 12, 0.5):
    print(i)
