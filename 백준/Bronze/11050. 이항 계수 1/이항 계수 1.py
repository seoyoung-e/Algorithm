from itertools import combinations

n,r = map(int, input().split())
combs = list(combinations(range(1, n + 1), r))  
print(len(combs))