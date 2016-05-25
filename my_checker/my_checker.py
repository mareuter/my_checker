def check_math(expression, answer):
    """Check a math expression with an answer.

    >>> import my_checker
    >>> if my_checker.check_math(6 * 9 - 12, 42):
    ...     print("The answer!")
    ... else:
    ...     print("Sorry for the inconvenience.")
    ...
    The answer!

    Parameters
    ----------
    expression : math equation
        The math expression to check.
    answer : numeric
        The answer to the expression.

    Returns
    -------
    bool
        True if answer matches evaluated equation, False if not.
    """
    return expression == answer
