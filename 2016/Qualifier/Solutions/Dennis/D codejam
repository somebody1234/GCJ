#!/usr/bin/env python3

def solve(KCS):
	K, C, S = map(int, KCS.split())
	tests = range(K)
	tiles = []

	while tests:
		test = tests[:C]
		tests = tests[C:]
		tiles.append(1 + sum((K ** pos * val) for (pos, val) in enumerate(test)))

	if len(tiles) > S:
		return 'IMPOSSIBLE'

	return ' '.join(map(str, tiles))

for case in range(1, int(input()) + 1):
	print('Case #', case, ': ', solve(input()), sep = '')