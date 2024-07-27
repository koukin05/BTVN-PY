n = input()

a = n.split()

q = [x.title() for x in a]

p = ' '.join(q)

print(p)
