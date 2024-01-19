
def isFloat(token):
    try:
        float(token)
        return '.' in token

    except ValueError:
        if token.count('.') > 1:
            raise ValueError(f"dots are not valid ")
        return False

