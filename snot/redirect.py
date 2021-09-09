import sys
from io import StringIO



out = StringIO()

sys.stdout = out

print('booger is snot')

sys.stdout = sys.__stdout__

print('printing out buffer contents')
print(out.getvalue() == 'booger is snot\n')
