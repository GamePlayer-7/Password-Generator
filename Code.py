import random
import string

print('Welcome to Password generator!')

numalpha=int(input('\nNumber of alphabets: '))
numdigits=int(input('Number of Digits: '))
numspchar=int(input('Number of Special characters: '))

if numalpha+numdigits+numspchar >= 8:
  tempalpha=tempdigits=tempspchar=''
  
 for i in range(numalpha):
    tempalpha=tempalpha+(random.choice(string.ascii_letters))
  for i in range(numdigits):
    tempdigits=tempdigits+(random.choice(string.digits))
  for i in range(numspchar):
    tempspchar=tempspchar+(random.choice('!@$%^&*?'))

    password=tempalpha+tempdigits+tempspchar
