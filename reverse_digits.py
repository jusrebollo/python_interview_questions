# Reverse a given integer

def reverse(x: int ) -> int:
    result, x_remainder = 0, abs(x)

    while x_remainder:
        result = result * 10 + x_remainder % 10
        x_remainder //=10

    return -result if x <0 else result


print(reverse(9274810))