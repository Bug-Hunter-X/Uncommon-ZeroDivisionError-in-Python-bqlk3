def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError, but only when x is 0
    else:
        return x / y

result = function_with_uncommon_error(0, 5)
print(result)