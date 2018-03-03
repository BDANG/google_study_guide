import math

def partition(nums, left, right, pivot):
    while left <= right:
        while nums[left] < pivot:
            left += 1

        while pivot < nums[right]:
            right -= 1

        if left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left+=1
            right-=1

    return left




def sort(nums, left=None, right=None):
    if left == None and right == None:
        sort(nums, 0, len(nums)-1)
        return

    if left >= right:
        return

    pivotIndex = math.floor((left+right)/2)
    pivot = nums[pivotIndex]

    i = partition(nums, left, right, pivot)

    sort(nums, left, i - 1)
    sort(nums, i, right)


x = [2, 8, 7, 4, 3, 5, 4]
sort(x)
print(x)
