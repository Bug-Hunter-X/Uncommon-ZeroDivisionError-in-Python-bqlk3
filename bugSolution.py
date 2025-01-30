def function_with_uncommon_error_fixed(x, y):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        else:
            return x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error in another way

result = function_with_uncommon_error_fixed(0, 5)
print(result)

result2 = function_with_uncommon_error_fixed(5,0)
print(result2)