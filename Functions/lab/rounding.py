sequence_of_numbers = input().split()


def rounded_number(numbers):
    result = []
    for number in sequence_of_numbers:
        current_number = round(float(number),)
        result.append(current_number)
    return result


print(rounded_number(sequence_of_numbers))