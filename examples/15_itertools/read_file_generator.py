def file_gen(filename):
    with open(filename) as f:
        for idx, line in enumerate(f):
            print(idx)
            yield line
