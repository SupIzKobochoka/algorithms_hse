def test(tracer):
    @tracer
    def fibonacci(num: int) -> int:
        if num in [1, 2]:
            return num - 1
        return fibonacci(num-1) + fibonacci(num-2)

    @tracer
    def cumsum(nums: list) -> float|int:
        if len(nums) == 1:
            return nums[0]
        return nums[-1] + cumsum(nums[:-1])


    fibonacci_aswers = {
        1: '''fibonacci(1)=0''',
        4: '''
fibonacci(4)=2
  fibonacci(3)=1
    fibonacci(2)=1
    fibonacci(1)=0
  fibonacci(2)=1'''[1:],
        5: '''
fibonacci(5)=3
  fibonacci(4)=2
    fibonacci(3)=1
      fibonacci(2)=1
      fibonacci(1)=0
    fibonacci(2)=1
  fibonacci(3)=1
    fibonacci(2)=1
    fibonacci(1)=0'''[1:]
    }

    cumsum_aswers = {
        (1,): 'cumsum([1])=1',
        (1, 2, 3): '''
cumsum([1, 2, 3])=6
  cumsum([1, 2])=3
    cumsum([1])=1'''[1:]
    }

    for num in fibonacci_aswers:
        _, result = fibonacci(num)
        assert result == fibonacci_aswers[num], f'''with 
@tracer
def fibonacci(num: int) -> int:
    if num in [1, 2]:
        return num - 1
    return fibonacci(num-1) + fibonacci(num-2)
and {num=}, expected \n{fibonacci_aswers[num]}, got \n{result}'''

    for arr in cumsum_aswers:
        _, result = cumsum(list(arr))
        assert result == cumsum_aswers[arr], f'''with 
@tracer
def cumsum(nums: list) -> float|int:
    if len(nums) == 1:
        return nums[0]
    return nums[-1] + cumsum(nums[:-1])         
and {arr=}, expected \n{cumsum_aswers[arr]}, got \n{result}'''
    