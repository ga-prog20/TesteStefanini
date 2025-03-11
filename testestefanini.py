def get_sign(num):
    if num > 0:
        return f"{num} is positive."
    elif num < 0:
        return f"{num} is negative."
    return f"{num} is zero."

def get_parity(num):
    return f"{num} is even." if num % 2 == 0 else f"{num} is odd."

def is_divisible_by_3(num):
    return f"{num} is divisible by 3." if num % 3 == 0 else f"{num} is not divisible by 3."

def check_number(num):
    return f"{get_sign(num)} {get_parity(num)} {is_divisible_by_3(num)}"

def main():
    try:
        number = int(input("Enter a number: "))
        print(check_number(number))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
