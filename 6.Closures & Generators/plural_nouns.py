__author__ = 'PyBeaner'

import re

def plural(noun):
    for match_rule,apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)


def build_match_and_apply_function(pattern,search,replace):
    def match_rule(word):
        return re.search(pattern,word)

    def apply_rule(word):
        return re.sub(search,replace,word)

    return match_rule,apply_rule

rules = []
with open("plural-rule.txt") as file:
    for line in file:
        pattern,search,replace = line.split(None,3) # split by any whitespaces, and take 3 sections
        rules.append(build_match_and_apply_function(
            pattern,search,replace))


if __name__ == "__main__":
    print(plural("fox"))
    print(plural("boy"))
    print(plural('vacancy'))