import re

def read_file(path):
    with open(path, 'r',encoding = 'utf-8') as file:
        return file.read().splitlines()

def extract_calibration_value(code):
    if (code == ''): raise ValueError('the line is an empty string')
    any_digit_pattern = re.compile('[0-9]')
    digits = any_digit_pattern.findall(code)

    return int(digits[0] + digits[-1])
    
def get_solution():
    lines = read_file('./puzzle-input.txt')
    total = 0
    for line in lines:
        total += extract_calibration_value(line)
    return total


print(get_solution())

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet


