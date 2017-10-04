

def add(nums):
    total = 0

    for num in nums:
        total = total + num
    return total

def subtract(nums):
    total = nums[0]

    for num in nums[1:]:
        total = total - num  
    return total

def multiply(nums):
    total = 1

    for num in nums:
        total = total * num 
    return total

def divide(nums):
    total = nums[0]

    for num in nums[1:]:
        total =  total / num 
    return total

def square(nums):

    num_list = []
    for num in nums:
        num_list.append(num * num)

    return num_list

def cube(nums):

    num_list = []
    for num in nums:
        num_list.append(num ** 3)

    return num_list

def power(nums):
    total = nums[0]

    for num in nums[1:]:
        total =  total ** num 
    
    return total

def mod(nums):
    total = nums[0]

    for num in nums[1:]:
        total =  total % num 
    
    return total

def add_mult(nums):
    total = (nums[0] + nums[1]) * nums[2]
    return total


def add_cubes(nums):
    total = 0

    for num in nums:
        total = total + num ** 3
    return total


