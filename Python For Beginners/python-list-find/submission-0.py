from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    count = len(nums)
    i = 0
    while(count>0):
        if(nums[i]==target):
            return i
        else:
            i += 1
            count -= 1    



# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

