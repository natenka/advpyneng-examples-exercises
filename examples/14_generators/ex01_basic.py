def generate_nums(number):
    print('Start of generation')
    yield number
    print('Next number')
    yield number + 1
    print('The end')



