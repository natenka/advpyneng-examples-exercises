def count_total(start_value=0):
    total = [start_value]
    def inner(add_number):
        total.append(add_number)
        return sum(total)
    return inner


def count_total2(start_value=0):
    total = start_value
    def inner(add_number):
        nonlocal total
        total += add_number
        # total = total + add_number
        return total
    return inner


