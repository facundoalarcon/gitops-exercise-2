import pytest
from conduit import urls
def test_file1_method1():
	x=5
	y=6
	r = 11
	z = sum(x,y)
	assert z == r,"test failed"
