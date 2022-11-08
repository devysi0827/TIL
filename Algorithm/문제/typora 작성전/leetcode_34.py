
def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]
    else:
        start = 0
        end = len(nums) - 1

    while start < end:
        mid = int((start + end) // 2)

        if nums[mid] == target:
            start = mid
            end = mid
            break
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid

    for i in range(start, -1, -1):
        if nums[i] == target:
            start = i
        else:
            break

    for i in range(end, len(nums)):
        if nums[i] == target:
            end = i
        else:
            break

    return [start, end]

nums = [1,4]
target = 4

print(searchRange(nums,target))