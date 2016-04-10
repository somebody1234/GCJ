import unittest


DIGITS = set(range(10))


def digits(n):
    return set(int(c) for c in str(n).strip('-.'))


def sleep(n):
    if n == 0:
        return 'INSOMNIA'
    step = 1
    m = n
    seen = digits(m)
    while True:
        if seen == DIGITS:
            return m
        step += 1
        m = n * step
        seen |= digits(m)


def read_tests(fobj):
    n = int(fobj.readline().strip())
    for _ in range(n):
        yield int(fobj.readline().strip())


def do_test(cur, n):
    return 'Case #{0}: {1}'.format(cur, sleep(n))


def main():
    import sys
    for idx, test in enumerate(read_tests(sys.stdin)):
        print(do_test(idx+1, test))
        sys.stdout.flush()


class TestA(unittest.TestCase):
    cases = [(0, 'INSOMNIA'),
             (1, 10),
             (2, 90),
             (11, 110),
             (1692, 5076)]

    def test_cases(self):
        for case in self.cases:
            self.assertEqual(sleep(case[0]), case[1], 'sleep({0}) -> {1}'.format(*case))

    def test_digit_constant(self):
        self.assertSetEqual(DIGITS, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

    def test_digits(self):
        self.assertSetEqual(digits(1234), {1, 2, 3, 4})
        self.assertSetEqual(digits(1234567890), DIGITS)


if __name__ == '__main__':
    main()

