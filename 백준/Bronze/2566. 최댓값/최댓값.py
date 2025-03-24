import sys

max_num = 0
idx = (0, 0)

for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    row_max = max(row)
    if row_max > max_num:
        max_num = row_max
        idx = (i, row.index(row_max))

print(max_num)
print(idx[0] + 1, idx[1] + 1) 
    