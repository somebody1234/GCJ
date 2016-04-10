#!/usr/bin/env python3

def solve(N):
	N = int(N)
	multiple = 0
	digits = set()

	if not N:
		return 'INSOMNIA'

	while True:
		multiple += N
		digits |= set(str(multiple))
		if len(digits) == 10:
			return multiple
		

for case in range(1, int(input()) + 1):
	print('Case #', case, ': ', solve(input()), sep = '')