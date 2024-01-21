def isFloat(token):
    """
    Check if a given string can be converted to a float.

    :param token: The string to be checked.
    :return: True if the string can be converted to a float, False otherwise.
    :raises ValueError: If the string contains more than one dot.
    """

    try:
        float(token)
        return '.' in token

    except ValueError:
        if token.count('.') > 1:
            raise ValueError(f"dots are not valid ")
        return False
