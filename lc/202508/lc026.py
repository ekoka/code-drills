def remove_duplicates(nums):
    write = 1
    read = 1
    while read < len(nums):
        if nums[read]!=nums[read-1]:
            nums[write] = nums[read]
            write += 1
        read += 1
    rem = write
    while rem < len(nums):
        nums[rem] = '_'
        rem += 1
    return write

def remove_duplicates(nums):
    write = 1
    read = 1
    while read < len(nums):
        if nums[read] > nums[read-1]:
            nums[write] = nums[read]
            write += 1
        read += 1
    return write

