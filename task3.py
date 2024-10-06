import re


def normalize_phone(phone_number):
    # The function formats numbers into the correct form.
    # The function returns the formatted phone number (list item) and is executed as many times 
    # as there are items in the list.
    # Finds the “+” character and numbers in the string and deletes other symbols.
    phone_number = re.sub(r"[^\+\d]", "", phone_number)
    # Checks for country code (38).
    if phone_number.startswith("38"):
        phone_number = "+" + phone_number
        return phone_number
    # Checks for the presence of the “+” character.
    elif phone_number.startswith("+"):
        return phone_number
    # Otherwise adds the “+” character and the country code.
    else:
        phone_number = "+38" + phone_number
        return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS campaigns: ", sanitized_numbers)