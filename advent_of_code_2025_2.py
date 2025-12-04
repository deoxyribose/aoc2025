import re

# input_ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input_ids = "17330-35281,9967849351-9967954114,880610-895941,942-1466,117855-209809,9427633930-9427769294,1-14,311209-533855,53851-100089,104-215,33317911-33385573,42384572-42481566,43-81,87864705-87898981,258952-303177,451399530-451565394,6464564339-6464748782,1493-2439,9941196-10054232,2994-8275,6275169-6423883,20-41,384-896,2525238272-2525279908,8884-16221,968909030-969019005,686256-831649,942986-986697,1437387916-1437426347,8897636-9031809,16048379-16225280"

ids = [id.split('-') for id in input_ids.split(',')]

# check for repeated numbers
# def is_repeated(num_str):
#     half_len = len(num_str) // 2
#     return num_str[:half_len] == num_str[half_len:]
def is_only_one_or_more_repeats(s):
    """
    Check if the string consists of a digit sequence repeated more than once.
    """
    pattern = r'^(\d+)\1+$'
    return re.match(pattern, s) is not None


invalid_ids = []
for start, end in ids:
    for num in range(int(start), int(end) + 1):
        num_str = str(num)
        # if is_repeated(num_str):
        if is_only_one_or_more_repeats(num_str):
            invalid_ids.append(num_str)

# print(invalid_ids)

print(f"Total valid IDs: {sum(map(int, invalid_ids))}")