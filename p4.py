# Find runner-up from given list

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])

# D21CS105
# Atharva Joshi