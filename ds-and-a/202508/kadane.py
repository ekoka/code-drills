def maxsum(array):
    n = len(array)
    if n==0: return

    running_sum = array[0]
    maxsum = running_sum
    i = 1
    while i < n:
        running_sum = max(running_sum + array[i], array[i])
        maxsum = max(maxsum, running_sum)
        i += 1

