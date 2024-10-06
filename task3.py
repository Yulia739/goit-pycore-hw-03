import re

def normalize_phone(phone_number):
    pattern = r"+38.+ \d+"
    match = re.search(pattern, phone_number)
    if match:
        print("match: ", match.group())

    #clean = phone_number.strip()
    #print(clean)

    
    # if phone_number.startswith('+'):
    #     pass
    # else: phone_number = f"+ {phone_number}"



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