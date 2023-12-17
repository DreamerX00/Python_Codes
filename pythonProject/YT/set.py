#n = set()
#print(type(n))

N_is_a_set_of= {2,4,6,8,10,12}
#print(N_is_a_set_of)
N = N_is_a_set_of
#print(N)
N.add(14)
S = { 16, 18, 20, 22, 24, 26, 28,}
#N.union(S)
S2 = {2, 5, 7, 13, 17, 19, 23, 29, 33, 39,}

S3 = {}

S.remove(22)





print(N.union(S), N.intersection(S2), N.isdisjoint(S3), N.difference(), N.symmetric_difference(S3))