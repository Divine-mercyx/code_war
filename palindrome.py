def is_palindrome(number):
    converted_number = str(number)
    reversed_number = converted_number[::-1]
    return reversed_number == converted_number


print(is_palindrome(124))
