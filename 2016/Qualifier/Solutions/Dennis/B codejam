#!/usr/bin/env python3

def solve(S):
	flips = 0
	last = '+'

	for pancake in S[::-1]:
		flips += (pancake != last)
		last = pancake

	return flips

for case in range(1, int(input()) + 1):
	print('Case #', case, ': ', solve(input()), sep = '')