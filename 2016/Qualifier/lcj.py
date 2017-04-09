import re
from random import random
from collections import deque
from functools import lru_cache, reduce

BASE_DIGITS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
_lcj_case = 1
R_CASE = re.compile(r'Case #\d+:\s+')

## Tips
# To add sets, do set | set

## Python 3 tips
# To convert from set to list easily and vice versa, use {*list} and [*set]

## Summary

# Jam
# lines(letter)           all lines of latest input of $letter but first
# openw()                 a file object opened for output
# testify(lines)          a list of lists containing the testcases, where testcases are preceded by the number of lines

# Arrays
# chunk(arr, length)      $arr split into chunks of length $length, and adds the rest
# dedup(arr)              $arr with all but the first of consecutive repeated elements removed
# casta(arr, ctor)        a new object of type $ctor, with $arr as sole argument
# inta(arr)               $arr with all elements cast to integer
# stra(arr)               $arr with all elements cast to string

# Primality
# trialFactor(n, limit=1) 0, or the smallest prime factor of $n under $limit (exclusive), or 0 if not found

# Base
# revbasea(arr, base)     $arr with base $base converted to an integer
# revbases(s, base)       $str with base $base converted to an integer
# basea(n, base)          $n converted to array with base $base
# bases(n, base)          $n converted to string with base $base
# bins(n)                 $n converted to a binary string
# bina(n)                 $n converted to a binary array
# octs(n)                 $n converted to a octal string
# octa(n)                 $n converted to a octal array
# decs(n)                 $n converted to a decimal string
# deca(n)                 $n converted to a decimal array
# hexs(n)                 $n converted to a hexadecimal string
# hexa(n)                 $n converted to a hexadecimal array

# Sequences
# fib(n)                  term number $n of the Fibonacci sequence
# lucas(n)                term number $n of the Lucas sequence

# Misc
# rand(n=1)               a random number between 0 and 1 inclusive, or a random integer between 0 and $n inclusive

# Generators
# muls(n, start=1)        a generator that returns multiples of $n, starting with the $start-th

## Jam

def lines(letter):
	lines = _lcj_lines(letter + '-large.in')
	if lines:
		return [line[:-1] for line in lines]
	i = 100
	while i>-1:
		lines = _lcj_lines(letter + '-small-2-attempt' + str(i) + '.in')
		if lines:
			return [line[:-1] for line in lines]
		i -= 1
	i = 100
	while i>-1:
		lines = _lcj_lines(letter + '-small-1-attempt' + str(i) + '.in')
		if lines:
			return [line[:-1] for line in lines]
		i -= 1
	i = 100
	while i>-1:
		lines = _lcj_lines(letter + '-small-attempt' + str(i) + '.in')
		if lines:
			return [line[:-1] for line in lines]
		i -= 1
	raise IOError()

def openw():
	return open('IO/out','w+')

def _lcj_lines(path):
	try:
		with open('IO/'+path) as f:
			return f.readlines()[1:]
	except:
		return False

def testify(lines):
	result = []
	while lines:
		n = int(lines[0])
		result += [lines[1:n+1]]
		lines = lines[n+1:]
	return result

def outLines(n=-1):
	if n != -1:
		try:
			with open('../IO/out'+str(n)) as f:
				return [line.strip() for line in f.readlines()]
		except:
			return False
	while n<10:
		n += 1
		try:
			with open('../IO/out'+('' if n==0 else str(n))) as f:
				return [line.strip() for line in f.readlines()]
		except:
			pass
	return False

def remCase(lines):
	return filter(None, [R_CASE.sub(line, '') for line in lines])

def case(f, *obj):
	global _lcj_case
	f.write('Case #'+str(_lcj_case)+': ')
	if obj:
		for o in obj[:-1]:
			f.write(str(o)+' ')
		f.write(str(obj[-1]))
	f.write('\n')
	_lcj_case += 1

def maxLen(obj, length, err):
	return err if len(obj) > length else obj

## Arrays

def chunk(arr, length):
	returns = []
	while len(arr)>=length:
		returns.append(arr[:length])
		arr = arr[length:]
	if arr:
		returns.append(arr)
	return returns

def dedup(arr):
	i = 0; d = arr[0]; returns = arr[0]
	for c in arr[1:]:
		if c != d:
			returns += c
			d = c
	return returns

def casta(arr, ctor):
	return [ctor(obj) for obj in arr]

def inta(arr):
	return [int(obj) for obj in arr]

def stra(arr):
	return [str(obj) for obj in arr]

## Primality

def trialFactor(n, limit=-1):
	if n%2==0: return 2
	maximum = n**.5
	factor = 1
	while factor<maximum:
		factor += 2
		if n%factor == 0: return factor
		if limit>0 and factor>limit: return 0
	return 0

## Base

def revbasea(arr, base):
	n = 0
	while arr:
		n *= base
		n += arr[-1]
		del arr[-1]
	return n

def revbases(s, base):
	return revBaseArr([BASE_DIGITS.index(c) for c in s])

def basea(n, base): #assumes n is int
	arr = deque()
	while n:
		arr.appendleft(n%base)
		n //= base
	return list(arr)

def bases(n, base):
	return ''.join([BASE_DIGITS[c] for c in baseArr(n, base)])

def bins(n):
	return bin(n)[2:]

def bina(n):
	return [int(c) for c in bins(n)]

def octs(n):
	return oct(n)[1:]

def octa(n):
	return [int(c) for c in octs(n)]

def decs(n):
	return n[2:]

def deca(n):
	return [int(c) for c in n]

def hexs(n):
	return hex(n)[2:]

def hexa(n):
	return [BASE_DIGITS.index(c) for c in hexs(n)]

## Sequence

@lru_cache(maxsize=None)
def fib():
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

@lru_cache(maxsize=None)
def lucas():
    if n < 2:
        return 1 if n else 2
    return lucas(n - 1) + lucas(n - 2)

## Misc

def rand(n=1):
	if n == 1:
		return random()
	return int(random()*n)

## Generators

def muls(n, start=1):
	while 1:
		yield n * start
		start += 1