#!/usr/bin/env python3

print('Case #1:')
input()
N, J = map(int, input().split())

for i in range(J):
	half = bin(2 ** (N // 2 - 1) + i * 2 + 1)[2:]
	full = half * 2
	print(full, *[int(half, base) for base in range(2, 11)], sep = ' ')