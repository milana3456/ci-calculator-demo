def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b


def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a, b):
    """Возвращает частное двух чисел.
    При делении на ноль возбуждает ValueError."""
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b


def power(base, exponent):
    """Возвращает результат возведения числа в степень."""
    return base ** exponent