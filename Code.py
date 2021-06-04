import random
import string

print('Welcome to Password generator!')

numalpha=int(input('\nNumber of alphabets: '))
numdigits=int(input('Number of Digits: '))
numspchar=int(input('Number of Special characters: '))

if numalpha+numdigits+numspchar >= 8:
  tempalpha=tempdigits=tempspchar=''
