class InvalidArgument(Exception):
    pass


# 1 Implement a decorator @single_str_arg that validates that function received exactly one argument and that the argument type is string
def single_str_arg(other_function):
    def validator(*args, **kwargs):
        if isinstance(args[0], str) and (len(args[0]) > 0) and len(kwargs) == 0:
            result = other_function(*args)
            return result
        else:
            raise InvalidArgument()

    return validator


# 2 Implement a decorator @numeric_params that validates that function received only numeric arguments (int, float)

def numeric_params(other_function):
    def validator(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise InvalidArgument()
        return other_function(*args)
    return validator


# 3 Implement a decorator @valid_param_types that receives as parameter allowed
# argument types and validates whether the argument passed to a function answers this requirement

def valid_param_types(valid_params: list):
    def wrapper(other_function):

        def validator(*args, **kwargs):
            if (type(args[0]) and type(args[1])) in valid_params:
                result = other_function(*args, **kwargs)
                return result
            else:
                raise InvalidArgument()

        return validator

    return wrapper


# 4 Implement a decorator @numeric_in_range that receives as parameters allowed range for numeric arguments (2 numbers - min and max)
# and validates that all the numerical arguments passed to the decorated function are in the range specified

def numeric_in_range(min_val, max_val):
    def wrapper(other_function):
        def validation(*args):
            for arg in args:
                if isinstance(arg, (int, float)) and not (min_val <= arg <= max_val):
                    raise InvalidArgument()
            return other_function(*args)
        return validation
    return wrapper



# 1
@single_str_arg
def convert_str(word: str) -> str:
    return word.upper()

# 2
@numeric_params
def mull_numbers(num1, num2) -> int:
    return num1 * num2

# 3
@valid_param_types([int, float])
def sum_numbers(num1, num2) -> int:
    return num1 + num2

# 4
@numeric_in_range(1,8)
def percentage(value):
    return value



if __name__ == '__main__':
    print(convert_str("liav"))  # single_str_arg
    print(sum_numbers(1, 3))  # valid_param_types
    print(mull_numbers(True,"efe"))  # numeric_params
    print(percentage(5))  # numeric_in_range
