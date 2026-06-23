def verify_card_number(digits: str):
    digits = digits.replace(" ", "").replace("-","")
    digits = list(digits)
    digits = digits[::-1]


    for n in range(1, len(digits), 2):
        digits[n] = int(digits[n]) * 2
        if digits[n] > 9:
            digits[n] -= 9

    total = 0
    for x in digits:
        total += int(x)
        
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
