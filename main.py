import random
l1 = ['lemon', 'apple', 'mango', 'banana']

from decimal import Decimal

random.shuffle(l1)
print(random.choice(l1))
print(l1)

Decimal('0.1') + Decimal('0.1') + Decimal('0.1')

set_one = {'saqib', 'ali', 'umer'}
set_two = {'azan', 'ali', 'faiz'}

result = set_one | set_two

print(result)