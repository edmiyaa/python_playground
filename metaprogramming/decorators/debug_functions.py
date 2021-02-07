from functools import wraps, partial


def debug(func=None, *, prefix=''):
    """Decorator that prints the name of the function with an optional prefix."""
    if func is None:
        return partial(debug, prefix=prefix)

    @wraps(func)  # Copies function metadata (function name, docstring, etc.)
    def wrapper(*args, **kwargs):
        """This is the wrapper!"""
        # Prints the qualified name of function, preceded with optional prefix
        print(f'{prefix}{func.__qualname__}')
        return func(*args, **kwargs)
    return wrapper


@debug(prefix='***')  # Decorator with parameter
def add(x, y):
    """Adds two numbers."""
    return x + y


@debug  # Decorator without parameter
def sub(x, y):
    """Subtracts two numbers."""
    return x - y


def main():
    a = 6
    b = 2

    # Call decorated functions
    print(f'add of {a} and {b} is: {add(a, b)}\n')
    print(f'sub of {a} and {b} is: {sub(a, b)}\n')

    # Function metadata is kept if we use functools.wraps. Without it, we get
    # metadata from the wrapper function
    print(f'add function object: {add}')
    print(f'add function name: {add.__name__}')
    print(f'add function docstring: {add.__doc__}')
    print()
    print(f'sub function object: {sub}')
    print(f'sub function name: {sub.__name__}')
    print(f'sub function docstring: {sub.__doc__}')


if __name__ == '__main__':
    main()
