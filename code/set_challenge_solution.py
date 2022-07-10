english = set("AAABCDEFFGHIJKLLLLLLMNOPQRSTUVWXYZ")
hawaiian = set("AAAEHIKLMMMMNOPUW")

def union(a, b):
    for x in b:
        a.add(x)
    return a

def intersect(a, b):
    c = set()
    for x in a:
        if x in b:
            c.add(x)
    return c

union_alphabets = union(english, hawaiian)
print(union_alphabets)

intersect_alphabets = intersect(english, hawaiian)
print(intersect_alphabets)