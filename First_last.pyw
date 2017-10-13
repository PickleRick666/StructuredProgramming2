Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def first_last6(nums):
	return nums[0] == 6 or nums[-1] == 6

>>> first_last6([1, 2, 6])
True
>>> first_last6([6,1,2,3])
True
>>> first_last6([13,6,1,2,3])
False
>>> 
