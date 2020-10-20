print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__']

print(dir(__builtins__))
for m in dir(__builtins__):
    print(m)
# ArithmeticError AssertionError AttributeError BaseException BlockingIOError
# BrokenPipeError BufferError BytesWarning ChildProcessError ConnectionAbortedError
# ConnectionError

import shelve
print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'shelve']
print()
print(dir(shelve))
# ['BsdDbShelf', 'BytesIO', 'DbfilenameShelf', 'Pickler', 'Shelf',
# 'Unpickler', '_ClosedDict', '__all__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'collections', 'open']

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
# clear close get items keys pop popitem setdefault

help(shelve) #gives you quite a bit of info or do control and click on shelve

