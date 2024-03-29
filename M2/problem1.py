a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
a3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a4 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]



# UCID - dm767
# Date - Feb 6
# Explanation - The important function in this code is to find the modulus value during each iteration of I to see whether the value is even or odd.

def process_array(num, arr):
    result = []
    print("\nProcessing Array({}):".format(num))
    print(arr)
    print("\nOdds output:")
    # TODO add necessary print statement to output only the odd values (hint, best if shown as a single line)
    for i in arr:
        if i % 2 != 0:
            result.append(i)
    print(result)


print("Problem 1")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)