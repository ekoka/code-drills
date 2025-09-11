def kadane(array):
    running_sum = -float('inf')
    maxsum = running_sum
    for i in range(len(array)):
        running_sum = maxsum(running_sum + array[i], array[i])
        maxsum = max(maxsum, running_sum)
    return maxsum

def kadane(array):
    running_sum = -float('inf')
    maxsum = running_sum
    for v in array:
        running_sum = max(running_sum + v, v)
        maxsum = max(maxsum, running_sum)
    return maxsum
