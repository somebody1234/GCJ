sc = new Scanner(System.in)
1.upto(sc.nextInt()) {
	print "Case #$it:"
	k = sc.nextLong()
	c = sc.nextInt()
	s = sc.nextInt()
	tiles = []
	tile = 0l
	level = 0
	0.upto(k-1) {
		tile = tile * k + it
		if (++level == c) {
			tiles.add(tile)
			tile = 0l
			level = 0
		}
	}
	if (level > 0) {
		while (level < c) {
			tile *= k
			level++
		}
		tiles.add(tile)
	}
	if (tiles.size > s)
		print " IMPOSSIBLE"
	else
		tiles.each {
			print(" " + (it + 1))
		}
	println()
}
