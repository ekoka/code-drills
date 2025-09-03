"""
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:
    n == nums.length
    1 <= n <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
"""
def maxsum_circular(nums):
    n = len(nums)
    total_sum = sum(nums)
    running_max_sum = nums[0]
    running_min_sum = nums[0]
    total_max = running_max_sum
    total_min = running_min_sum

    for i in range(1, n):
        running_max_sum = max(running_max_sum+nums[i], nums[i])
        if running_max_sum > total_max:
            total_max = running_max_sum

        running_min_sum = min(running_min_sum+nums[i], nums[i])
        if running_min_sum < total_min:
            total_min = running_min_sum

    if total_max < 0: return total_max
    return max(total_sum - total_min, total_max)

def maxsum_circular(nums):
    total_sum = sum(nums)
    running_max_sum = nums[0]
    running_min_sum = nums[0]
    total_max = running_max_sum
    total_min = running_min_sum

    for i in range(1, len(nums)):
        running_max_sum = running_max_sum+nums[i] if running_max_sum > 0 else nums[i]
        if running_max_sum > total_max:
            total_max = running_max_sum
        running_min_sum = running_min_sum+nums[i] if running_min_sum < 0 else nums[i]
        if running_min_sum < total_min:
            total_min = running_min_sum
            
    if total_max < 0: return total_max
    return total_sum - total_min if total_sum - total_min > total_max else total_max

if __name__=='__main__':
    nums = [1,-2,3,-2]
    exp = 3
    res = maxsum_circular(nums)
    print(res)
    assert res==exp

    nums = [5,-3,5]
    exp = 10
    res = maxsum_circular(nums)
    print(res)
    assert res==exp

    nums = [-3,-2,-3]
    exp = -2
    res = maxsum_circular(nums)
    print(res)
    assert res==exp
