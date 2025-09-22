import re


def clean_phone_number(phone: str) -> str| None:
    """
    Cleans phone number from country code, if it is valid, and removes any non-numerical characters

    # Returns:
    * str = with cleaned phone number.
    * None = phone-number provided was invalid

    """
    if not phone:
        return None
    
    # strip from any leading and trailing spaces
    phone = phone.strip()

    # validate country code
    if phone.startswith('+7'):
        phone = phone[2:]
    elif phone.startswith('7'):
        phone = phone[1:]
    elif phone.startswith('8'):
        phone = phone[1:]
    else:
        return None

    # return numbers
    return re.sub(r'\D', '', phone)


def validate_phone_number(phone: str) -> bool:
    """
    Validates given phone number

    Returns: 
        `bool`: is phone valid
    """
    # clean number from irrelevant data
    digits: str | None = clean_phone_number(phone)

    if not digits:
        return digits

    area_code = int(digits[:3])

    # check if area code is valid
    if not (900 <= area_code <= 999) and area_code not in ["495", "800", "499", "812"]:
        return False

    return True


def validate_password(password: str) -> bool:
    """
    Validates provided password
    Returns:
        `bool` if provided password is valid
    """

    if not password:
        return False

    # Check length
    if not (6 <= len(password) <= 30):
        return False

    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_digits = bool(re.search(r'[0-9]', password))
    has_symbols = bool(re.search(r'[!@#]', password))

    # Count all types of checks that passed
    types_count = sum([has_lowercase, has_uppercase, has_digits, has_symbols])

    # Must have at least 3 out of 4 
    return types_count >= 3