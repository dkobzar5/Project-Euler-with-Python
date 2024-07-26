a1 = sum([pow(i,2) for i in range(1,101)])
a2 = pow(sum(i for i in range(1,101)),2)
print(a2-a1)