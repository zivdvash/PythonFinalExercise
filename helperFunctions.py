
def isFloat(token):
    try:
        float(token)
        return '.' in token
    except ValueError:
        return False

