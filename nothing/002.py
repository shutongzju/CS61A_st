"""Generalization"""

from math import pi

def area_square(r):
	assert r > 0, 'the length must be positive'
	return r * r

def area(r, shape_constant):
	assert r > 0, 'The length must be positive'
	return r * r * shape_constant

def summation 