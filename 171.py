stdin = open(0)
n = int(stdin.readline())
come_in = []
come_out = []

def conv_time(s) -> int:
    return int(s[:2]) * 60 + int(s[3:])

for i in range(n):
    come_in.append(conv_time(stdin.read(5)))
    stdin.read(1)
    come_out.append(conv_time(stdin.read(5)))
    stdin.read(1)

come_in.sort()
come_out.sort()
curr_in = 0
max_in = 0
curr_out = 0
for t in come_in:
    curr_in += 1
    while t > come_out[curr_out]:
        curr_in -= 1
        curr_out += 1
    if curr_in > max_in:
        max_in = curr_in
print(max_in)