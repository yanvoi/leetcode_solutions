class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = set("!@#$%^&*()-+")
        if len(password) < 8: return False
        if not any(char.islower() for char in password): return False
        if not any(char.isupper() for char in password): return False
        if not any(char.isdigit() for char in password): return False
        if not any(char in special for char in password): return False
        if any(a == b for a, b in zip(password, password[1:])): return False

        return True
