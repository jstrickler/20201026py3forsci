

def doit(a, b, c):
    print(a)
    print(b)
    print(c)
    print()

doit(1, 2, 3)
doit('a', 'b', 'c')

colors = ['purple', 'puce', 'mauve']

doit(*colors)  #  doit(colors[0], colors[1], colors[2])
