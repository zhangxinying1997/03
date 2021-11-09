def check_card_number(card_number:int)->bool:
    digits = []

    while card_number != 0:
        digits = [card_number % 10] + digits
        card_number = card_number // 10

    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)

    for d in even_digits:
        d_0 = 2 * d
        d_1 = d_0 // 10
        d_2 = d_0 % 10
        checksum += d_1
        checksum += d_2

    return checksum % 10 == 0

if __name__ == '__main__':
    assert check_card_number(5082337440657928)
    assert not check_card_number(4601496706376197)

    print(check_card_number(5082337440657928))
    print(check_card_number(4601496706376197))

