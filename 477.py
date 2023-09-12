stdin = open(0)
ds = sum(int(c) for c in stdin.readline()[:-1])
if ds % 3 == 0:
    print(2)
else:
    print(1, ds % 3, sep="\n")