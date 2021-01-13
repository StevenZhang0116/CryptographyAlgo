import sys
import math
import gmpy2

from gmpy2 import mpz
from gmpy2 import invert
from gmpy2 import powmod
from gmpy2 import divm

def compute_x0s(p, h, g, B):
	return ((i, powmod(g, B*i, p)) for i in range(B))

# Compute x s.t. h = g^x mod p
def discrete_log(p, h, g, maxE = 40):
	B = mpz(2**(int(maxE/2)))
	g = mpz(g)
	h = mpz(h)
	p = mpz(p)

	x1s = {divm(h, powmod(g, i, p), p): i for i in range(B)}

	for x0, expr in compute_x0s(p, h, g, B):
		x1 = x1s.get(expr)
		if x1 is not None:
			print(f"x0: {x0}")
			print(f"x1: {x1}")
			return mpz(x0) * B + mpz(x1)

	raise ValueError("No suitable values found")

if __name__ == "__main__":
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

	x = discrete_log(p, h, g, 40)
	assert(h == powmod(g, x, p))
	print(f"x: {x}")
	print("Test Passed")
	print("")