a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    newarr = []
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    for i in arr:
        if type(i) == str:
            i = int(i)
            if i > 0:
                i = str(i)
                newarr.append(i)
            else:
                newarr.append(str(abs(i)))
        else:
            if i > 0:
                newarr.append(i)
            else:
                newarr.append(abs(i))
    [print(f"{v} {type(v)}, ") for v in newarr]


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)