def convert_to_lower(items):
    result = []
    for item in items:
        result.append(str(item).lower())
    return result


for i in convert_to_lower(["USER", "TEST", "Data"]):
    print(i)



def g_convert_to_lower(items):
    for item in items:
        yield str(item).lower()


iterator_1 = g_convert_to_lower(["USER", "TEST", "Data"])
for i in iterator_1:
    print(i)
