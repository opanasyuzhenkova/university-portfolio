import concurrent.futures


def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    user_input = int(input("Enter a number to calculate its factorial: "))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(calculate_factorial, user_input)
        print("Calculating factorial...")
        result = future.result()

    print(f"The factorial of {user_input} is {result}")


if __name__ == "__main__":
    main()
