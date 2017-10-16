def reverse_tuple(tup):
    tup1 = ()
    for x in range(len(tup)-1,-1,-1):
        print(x)
        tup1 += (tup[x],)
    return tup1

print(reverse_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9)))
