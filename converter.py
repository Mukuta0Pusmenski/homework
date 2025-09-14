def to_decimal(number_str, base):
    """
    Перетворює число з довільної системи числення у десяткову.
    Показує кроки множення розрядів.
    """
    digits = "0123456789ABCDEF"
    number_str = number_str.upper()
    decimal_value = 0
    steps = []

    for i, digit in enumerate(reversed(number_str)):
        value = digits.index(digit)
        step_value = value * (base ** i)
        decimal_value += step_value
        steps.append(f"Розряд {digit} * {base}^{i} = {step_value}")

    steps.reverse()
    return decimal_value, steps


def from_decimal(number, base):
    """
    Перетворює десяткове число у довільну систему числення.
    Показує кроки ділення з остачею.
    """
    digits = "0123456789ABCDEF"
    steps = []
    result = ""

    if number == 0:
        return "0", ["0 у будь-якій системі = 0"]

    while number > 0:
        quotient = number // base
        remainder = number % base
        steps.append(f"{number} ÷ {base} = {quotient}, остача = {remainder} ({digits[remainder]})")
        result = digits[remainder] + result
        number = quotient

    steps.reverse()
    return result, steps


def main():
    print("=== Перетворення чисел між системами числення ===")
    from_base = int(input("Введіть систему числення вихідного числа (2, 8, 10, 16): "))
    number_str = input(f"Введіть число у системі {from_base}: ")
    to_base = int(input("Введіть систему числення для перетворення (2, 8, 10, 16): "))

    print("\n=== Кроки перетворення ===")

    # Спочатку переводимо у десяткову
    if from_base != 10:
        decimal_value, steps_to_dec = to_decimal(number_str, from_base)
        print("\nПеретворення у десяткову:")
        for step in steps_to_dec:
            print("  " + step)
        print(f"Результат у десятковій: {decimal_value}")
    else:
        decimal_value = int(number_str)

    # Якщо цільова система не десяткова — переводимо далі
    if to_base != 10:
        result, steps_from_dec = from_decimal(decimal_value, to_base)
        print(f"\nПеретворення з десяткової у {to_base}-кову:")
        for step in steps_from_dec:
            print("  " + step)
        print(f"Результат у системі {to_base}: {result}")
    else:
        print(f"\nКінцевий результат у десятковій: {decimal_value}")


if __name__ == "__main__":
    main()
