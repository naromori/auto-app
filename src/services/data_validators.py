import re


class DataValidators:

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        if not phone:
            return False

        phone = phone.strip()

        # Check if starts with +7, 7, or 8
        if phone.startswith('+7'):
            phone = phone[2:]
        elif phone.startswith('7'):
            phone = phone[1:]
        elif phone.startswith('8'):
            phone = phone[1:]
        else:
            return False

        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)

        # Should have exactly 10 digits after country code
        if len(digits) != 10:
            return False

        # Check if first 3 digits (area code) are between 900-999
        area_code = int(digits[:3])
        if not (900 <= area_code <= 999):
            return False

        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        if not password:
            return False

        # Check length
        if not (6 <= len(password) <= 30):
            return False

        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'[0-9]', password))
        has_symbols = bool(re.search(r'[!@#]', password))

        # Count how many types are present
        types_count = sum([has_lowercase, has_uppercase, has_digits, has_symbols])

        # Must have at least 3 out of 4 types
        return types_count >= 3