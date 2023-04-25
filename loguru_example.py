from loguru import logger

def divide(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Attempted to divide by zero: {a} / {b}")
        return None

def main():
    logger.add("application.log", rotation="10 MB")

    numbers = [(10, 5), (4, 2), (9, 0), (7, 3)]

    for num1, num2 in numbers:
        divide(num1, num2)

if __name__ == "__main__":
    main()
