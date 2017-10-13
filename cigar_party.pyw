Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  return 40 <= cigars <= 60

>>> cigar_party(30, False)
False
>>> cigar_party(50, False)
True
>>> cigar_party(70, True)
True
>>> 
