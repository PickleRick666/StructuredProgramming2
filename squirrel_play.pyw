Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90

>>> squirrel_play(70, False)
True
>>> squirrel_play(95, False)
False
>>> squirrel_play(95, True)
True
>>> 
