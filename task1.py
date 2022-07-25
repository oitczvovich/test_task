def task(array):
    if not array:
        return('не верное значение, введите строку из 0 и 1')
    for c in range(len(array)):
        if int(array[c]) == 0:
            return(c)


print(task("111111111110000000000000000"))
