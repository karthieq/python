nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [n for n in nums] # list comprehension
print(lst)

lst = [n*n for n in nums] # list comprehension
print(lst)

lst = [n for n in nums if n%2 == 0] # list comprehension
print(lst)

lst = [(letter, num) for letter in 'abc' for num in range(4)] # list comprehension
print(lst) # list
print(lst[0][0]) # tuple
print(type(lst[0])) # tuple

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]

hsh = {key: val for key, val in zip(lst1,lst2)} # dict comprehension
print(hsh)

hsh = {key: val for key, val in zip(lst1,lst2) if key != 'c'} # dict comprehension
print(hsh)

nums = [1, 1, 2, 2, 3, 3, 4, 4]
lst = {n for n in nums} # set comprehension
print(lst)
print(type(lst))

nums = [1, 2, 3, 4, 5]
gen = (n*n for n in nums) # generator expression round brackets for generator functions
print(gen)
for g in gen:
    print(g)
