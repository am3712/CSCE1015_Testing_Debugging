import random

def calculate_average(numbers):
    total_sum = sum(numbers)
    count = len(numbers)   # FIX: removed -1
    average = total_sum / count
    return average

def generate_random_numbers(n):
    numbers = []
    for i in range(n):
        number = random.randint(1, 100)   # FIX: 101 → 100
        numbers.append(number)
    return numbers

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:   # FIX: was wrong condition
            even_numbers.append(num)
    return even_numbers

def main():
    numbers = generate_random_numbers(10)
    print("Generated numbers:", numbers)

    average = calculate_average(numbers)
    print("Average of numbers:", average)

    even_numbers = filter_even_numbers(numbers)
    print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()
