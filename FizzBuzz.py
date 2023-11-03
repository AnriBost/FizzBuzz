def fizzbuzz(input):
    if input % 2 == 0:
        return 'Fizz'
    if input % 3 == 0:
        return 'Buzz'
    if input % 2 ==0 and input % 3 == 0:
        return 'FizzBuzz'
print(fizzbuzz(8))