def mergesort(itemlist):
    # Python will innately round down if uneven list.
    if len(itemlist) <= 1:
        return itemlist

    half = len(itemlist) / 2
    a_list = itemlist[:half]
    b_list = itemlist[half:]

    a_list = mergesort(a_list)
    b_list = mergesort(b_list)
    c_list = []

    a_index = 0
    b_index = 0
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] >= b_list[b_index]:
            c_list.append(b_list[b_index])
            b_index += 1
        else:
            c_list.append(a_list[a_index])
            a_index += 1

    if a_index > len(a_list) - 1:
        c_list += (b_list[b_index:])
    else:
        c_list += (a_list[a_index:])

    return c_list


if __name__ == "__main__":
    samp = [1, 5, 9, 3, 2, 8, 6, 7, 4]
    print "Initial: ", samp
    final = mergesort(samp)
    print "Final: ", final
    import timeit
    print timeit.repeat("""mergesort(%r)""" % samp, """from __main__ import mergesort""", number=10000)
