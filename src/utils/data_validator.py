import re


class DataValidator:

    @staticmethod
    def clean_phone_number(phone: str) -> str:

        if not phone:
            return ""
        
        phone = phone.strip()

        if phone.startswith('+7'):
            phone = phone[2:]
        elif phone.startswith('7'):
            phone = phone[1:]
        elif phone.startswith('8'):
            phone = phone[1:]
        else:
            return ""

        return re.sub(r'\D', '', phone)


    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        
        digits = DataValidator.clean_phone_number(phone)

        if len(digits) != 10:
            return False

        area_code = int(digits[:3])
        if not (900 <= area_code <= 999) and area_code not in ["495", "800", "499", "812"]:
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