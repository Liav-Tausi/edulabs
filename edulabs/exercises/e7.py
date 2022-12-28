from concurrent.futures import ProcessPoolExecutor
import time

# Implement a python program that gets from the user a list of big numbers, and counts the factorial of these numbers.
# You should perform the calculations as fast as possible and print the results to the user in a friendly manner immediately when the result is ready


def factorial_of(list_of_numbers: list) -> None:
    with ProcessPoolExecutor(max_workers=7) as executor:
        for item in list_of_numbers:
            executor.submit(factorial_ing, item)


def factorial_ing(item):
    fact = 1
    for number in range(1, item + 1):
        fact *= number
    print("Factorial of", item, "is", fact)


if __name__ == '__main__':
    try:
        start = time.perf_counter()
        factorial_of([1550 for _ in range(100_000)])
        end = time.perf_counter()
        print(f"{round(end - start, 2)} seconds")

    except Exception:
        quit()

