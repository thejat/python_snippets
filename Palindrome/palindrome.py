def is_palindrome(s):
	""" (str) -> bool

	Return True iff s is a palindrome.

	>>> is_palindrome('thejajeht')
	True
	>>> is_palindrome('arsenal')
	False
	>>> is_palindrome('roaor')
	True
	"""
	return palindrome_alg2(s)
	#return palindrome_alg1(s) and palindrome_alg2(s)

def palindrome_alg1(s):
	""" (str) -> bool

	Return True iff s is a palindrome.

	>>> is_palindrome('thejajeht')
	True
	>>> is_palindrome('arsenal')
	False
	>>> is_palindrome('roaor')
	True
	"""

	return reverse(s)==s

def reverse(s) :
	"""(str) -> str

	Reverse string s

	>>> reverse('hello')
	'olleh'
	>>>reverse('t')
	't'

	"""

	rev = ''
	for e in s:
		rev = e + rev
	return rev

def palindrome_alg2(s):
	""" (str) -> bool

	Return True iff s is a palindrome.

	>>> is_palindrome('thejajeht')
	True
	>>> is_palindrome('arsenal')
	False
	>>> is_palindrome('roaor')
	True
	"""

	for i in range(len(s)/2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True




def main():

	print is_palindrome('thejajeht')
	print is_palindrome('t')
	print is_palindrome('oooo')
	print is_palindrome('trt')
	print is_palindrome('tret')

if __name__=='__main__':
	main()