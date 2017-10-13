Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  return 1

>>> date_fashion(5, 10)
2
>>> date_fashion(5, 2)
0
>>> date_fashion(5, 5)
1
>>> 
