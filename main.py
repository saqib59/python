'''
100 days of code - Python
'''


list_comprehension = [i*i for i in range(4)]
list_comprehension_even = [i*i for i in range(4) if i%2==0]

print(list_comprehension)
print(list_comprehension_even)

# you can not have a default argument followed by a non default arguement
c_list = ['3', 4, 2, 42, 42,521, 51, 64];

# if '3' in c_list:
#     print("yes")

print(c_list[1:8:2]) # 2 is jump index