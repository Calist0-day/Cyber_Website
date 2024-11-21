import re
def verify_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    has_upper_case = re.search("[A-Z]", password);
    has_lower_case = re.search("[a-z]", password);
    has_number = re.search("[0-9]", password);
    has_symbol = re.search(r"[@$!%*?&/#]", password);

    strength = sum([bool(has_upper_case), bool(has_lower_case), bool(has_number), bool(has_symbol)])

    if strength < 2:
        return "weak"
    elif strength  <= 3:
        return "medium"
    return "strong"