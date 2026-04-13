"""
Write a function (sum_function) that takes a variable number of arguments using the asterisk (*) operator.

Initialize the output value to zero.

Loop through the parameter sent to the function and add up the numbers.

Return the value of the output.

Test it out on different number of integer values.
"""

"""A function that returns the average of the numbers sent to it.
A function that takes in a variable number of strings. It returns 3 numbers in the form of a tuple.
The 3 numbers are the length of (shortest, average and longest) word in the strings sent.
Create a function that would take variables of any type (strings lists etc...) 
and only sums the numbers that are (or could be) converted into an integer."""


def sum_function(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def avg_function(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def word_length_function(*strings):
    length_list = []
    for string in strings:
        length_list += [len(string)]

    shortest = min(length_list)
    longest = max(length_list)
    average = sum(length_list) / len(length_list)


    return average, shortest, longest

def sum_ints_function(*objects):
    sum = 0
    for obj in objects:
        try:
            sum += int(obj)
        except ValueError:
            continue


    return sum



    """for obj in objects:
        if isinstance(obj, int):
            sum += obj
        elif isinstance(obj, str):
            if obj.isdigit():
                sum += int(obj)"""

    return sum


if __name__ == '__main__':
    print(sum_ints_function(1, 2, "3", "4", "Michael", "Milk in fridge", "4"))
    # print(word_length_function("I love", 'Learning', 'Python', 'at 2AM!'))


