__author__ = 'PyBeaner'

import re
import itertools

def solve(puzzle):
    words = re.findall("[A-Z]+",puzzle.upper())
    unique_characters = set("".join(words))
    assert len(unique_characters)<=10,"Too many letters"
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = "".join(first_letters)+\
        "".join(unique_characters-first_letters)

    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in "0123456789")
    zero = digits[0]

    for guess in itertools.permutations(digits,len(characters)):  # 矩阵（从digits中，取出不含重复元素的序列：（1，3，4，5，2，0...））
        if zero not in guess[:n]:  # n is the words(first letters) count, first letters cannot be zero
            # map characters with the guessing digits
            # translate from a byte to another
            equation = puzzle.translate(dict(zip(characters,guess)))
            if eval(equation):
                return equation

if __name__ == "__main__":
    puzzle = "HAWAII + IDAHO + IOWA + OHIO == STATES"
    # puzzle = "SEND + MORE == MONEY"
    print(puzzle)
    solution = solve(puzzle)
    if solution:
        print(solution)

