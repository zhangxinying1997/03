
def get_nearest_lucky_ticket(ticket):
    rest = ticket % 11
    if rest == 0:
        return ticket
    elif rest <= 5:
        return ticket - rest
    else:
        return ticket + (11 - rest)

if __name__ == '__main__':
    assert get_nearest_lucky_ticket(111111) == 111111
    assert get_nearest_lucky_ticket(123321) == 123321
    assert get_nearest_lucky_ticket(123320) == 123321
    assert get_nearest_lucky_ticket(333999) == 334004

    print(get_nearest_lucky_ticket(111111))
    print(get_nearest_lucky_ticket(123321))
    print(get_nearest_lucky_ticket(123320))
    print(get_nearest_lucky_ticket(333999))