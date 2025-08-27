def square(nums):
    for num in nums:
        yield num*num

nums = [1, 2, 3, 4, 5]
sqns = square(nums) # generator function
for num in sqns:
    print(num)
# print(list(sqns))

sqns = (num*num for num in nums) # generator expression
print(next(sqns))
for num in sqns:
    print(num)
# print(list(sqns))
