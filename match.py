#import re
# s='we Will enijoyed 3a lot 420'
# print(re.match('420',s))
# print(re.match('we',s))


# n = input('Enter a number:')
# s = re.fullmatch('[6-9]\d{9}', n)
# if s:
#     print('Valid number')
# else:
#     print('Not a valid number')

# import re

# n = input('Enter a number:')
# if re.match('^[6-9]\d{9}$', n):
#     print('Valid number')
# else:
#     print('Not a valid number')

import re
s=input("enter mail Id")
m=re.fullmatch('[a-zA-Z0-9_.]*@gmail[.]com',s)
if  m!=None:
    print('valid')
else:
    print('invalid')