def even_sum(nums: str) -> int:
    nums = list(map(int, nums.split()))
    nums_sum = sum(nums)
    if nums_sum%2==0:
        return nums_sum
    
    min_odd = min(nums, key=lambda num: num if (num+1)%2==0 else float('inf'))
    return nums_sum - min_odd

if __name__ == '__main__':
    from custom_tests import test

    test(even_sum)
    