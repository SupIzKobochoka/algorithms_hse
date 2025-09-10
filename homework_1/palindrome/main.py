def is_palindrome(number: int) -> bool:
    digits = []
    while number!=0:
        digits.append(number%10)
        number //= 10

    def is_palindrome_list(digits: list[int], index=0) -> bool:
        if index*2 > len(digits) or len(digits)==0:
            return True
        if digits[index] != digits[-index-1]:
            return False
        else:
            return is_palindrome_list(digits, index+1)
         
    return is_palindrome_list(digits)


if __name__ == '__main__':    
    from custom_tests import test
    
    test(is_palindrome)


