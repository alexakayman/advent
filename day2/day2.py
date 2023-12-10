calibration = []
str_integers = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9]]
integers = ["0","1","2","3","4","5","6","7","8","9"]

# open file lmao
with open("input.txt", "r") as f:
    lines = f.readlines() 

    # convert lines into digits only
    for line in lines:
        # if str int in line, replace line with num relating to int
        for str_int in str_integers:
            # replace string number, like "one", with its int correspondint, like 1. 
            num_line = line.replace(str_int[0],str_int[1])
            print(num_line)
            calibration.append(num_line)

# remove non-integers
for char in line:
    if char not in integers:
        clean_line = ''.join(char for char in line if char in integers)
#         print(f"{i}: {clean_line} \t {line}")
calibration.append([clean_line])


# join the first digit and the last digit
two_digit_calibrated = []
for cleaned_set in calibration:
    for cleaned_line in cleaned_set:
        two_digit = cleaned_line[0] + cleaned_line[-1]
        # print(f"{two_digit}, {cleaned_line}")
        two_digit_calibrated.append(two_digit)

# print(two_digit_calibrated)

two_digit_sum = 0
for two_digit in two_digit_calibrated:
    two_digit = int(two_digit)
    two_digit_sum += two_digit

print(two_digit_sum)