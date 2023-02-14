def validate_option(user_input):
    try:
        if 0 <= int(user_input) <= 4:
            return True
    except ValueError:
        return False


def validate_amount(user_input):
    try:
        if float(user_input) > 0:
            return True
    except ValueError:
        return False
