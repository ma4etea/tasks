keys = ["a", "b", "c"]
size = 64
hash_table = [[] for _ in range(size)]

hashes = [hash(key) for key in keys]


for hash_, key in zip(hashes, keys):
    index = hash_ & (size - 1)
    hash_table[index].append(key)
    print(index, hash_)

print(hash_table)
index = hash("a") & (size - 1)
print(index, hash_table[index])