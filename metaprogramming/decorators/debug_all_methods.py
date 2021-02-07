from python_playground.metaprogramming.decorators.debug_functions import debug


def debug_all_methods(cls):
    """Decorates every method in cls.

    Doesn't apply to class or static methods.
    """

    # For every attribute in cls
    for key, val in vars(cls).items():
        # If it's a callable
        if callable(val):
            # Redefine it with the debug decorator
            setattr(cls, key, debug(val, prefix='***'))
    return cls


@debug_all_methods
class Test:

    def a(self):
        pass

    def b(self):
        pass


def main():
    t = Test()

    # Call decorated methods
    t.a()
    t.b()


if __name__ == '__main__':
    main()
