def find_mean(num1, num2, num3):
    pass  # Replace 'pass' with code
    mean = (num1 + num2 + num3) / 3
    return mean


def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    pass  # Replace 'pass' with code
    std = ((((num1 - mean) ** 2) + ((num2 - mean) ** 2) + ((num3 - mean) ** 2)) / 3 ** 0.5)
    return mean, std
