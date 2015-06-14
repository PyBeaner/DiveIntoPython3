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

patterns = (
    ("[sxz]$","$","es"),
    ("[^aeioudgkprt]h$","$","es"),
    ("(qu[^aeiou])y$","y$","ies"),
    ("$","$","s"),
)

rules = [build_match_and_apply_function(pattern,search,replace) for pattern,search,replace in patterns]

if __name__ == "__main__":
    print(plural("fox"))
    print(plural("boy"))
    print(plural('vacancy'))