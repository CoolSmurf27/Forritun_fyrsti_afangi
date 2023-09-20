def sum_of_divisors(number):
    divisor_sum = 0
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum

def decide(number):
    divisor_sum = sum_of_divisors(number)
    if divisor_sum > number:
        return f"{number} is abundant."
    elif divisor_sum < number:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."