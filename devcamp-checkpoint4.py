import math
from decimal import Decimal

# Exercise 1

my_list = ['apple', 'banana', 'plum', 100]
print(my_list)

my_nums = (10, 5, 0, 100, 5, 5)
print(my_nums)

my_price = 17.30
print(my_price)

number = 50
print(number)

my_decimal = Decimal(1.1)
print(my_decimal)

my_cars = {
    'brand': 'Opel',
    'price': 40000,
    'color': 'black',
}
print(my_cars)

# Exercise 2
rounded_num = math.ceil(my_price)
print(rounded_num)

# Exercise 3
my_price_sqrt = math.sqrt(my_price)
print(my_price_sqrt)

# Exercise 4
print(my_cars.get('brand'))

# Exercise 5
print(my_nums[1])

# Exercise 6
my_list.append(20)
print(my_list)

# Exercise 7
my_list[0] = 'pear'
print(my_list)


# Exercise 8
second_list = ['d', 'a', 'e', 'c', 'b']
second_list.sort()
print(second_list)

# Exercise 9
tuple_list = list(my_nums)
tuple_list.append('a')
my_nums = tuple(tuple_list)

my_nums = my_nums + ('b',)
print(my_nums)
