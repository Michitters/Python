def g_hello():
    yield 'Hello 1'
    yield 'Hello 2'
    yield 'Hello 3'

for w in g_hello():
    print(w)
