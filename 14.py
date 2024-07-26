def generate_chain(chain):
    if chain[-1] == 1:
        return chain
    if chain[-1] % 2 == 0:
        chain.append(chain[-1]//2)
    else:
        chain.append(3*chain[-1]+1)
    return generate_chain(chain)

# n = 1
result = 0
max_len = 0
for i in range(1,1_000_000):
    res = generate_chain([i])
    if len(res) > max_len:
        max_len = len(res)
        result = i
print(result)

