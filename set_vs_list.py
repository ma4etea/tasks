from datetime import datetime
coll = [i for i in range(10000000)]

set_coll = set(coll)





start = datetime.now()

ssss = [2134567, 1243783, 9866984, 5679899, 7865678]

res1 = [i for i in ssss if i in set_coll]

end = datetime.now()
print(f"set:{end-start}")

start = datetime.now()

ssss = [2134567, 1243783, 9866984, 5679899, 7865678]

res = [i for i in ssss if i in coll]

end = datetime.now()
print(f"list:{end-start}")