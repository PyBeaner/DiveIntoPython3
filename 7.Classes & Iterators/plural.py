__author__ = 'PyBeaner'

import re

def build_match_and_apply_function(pattern,search,replace):
    def match_rule(word):
        return re.search(pattern,word)

    def apply_rule(word):
        return re.sub(search,replace,word)

    return match_rule,apply_rule

class LazyRule:
    rules_filename = "plural-rules.txt"

    def __init__(self):
        self.pattern_file = open(self.rules_filename,encoding="utf-8")
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index+=1
        if len(self.cache)>=self.cache_index:
            return self.cache[self.cache_index]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern,search,replace = line.split(None,3)
        funcs = build_match_and_apply_function(pattern,search,replace)
        self.cache.append(funcs)
        return funcs


if __name__ == "__main__":
    r1 = LazyRule()
    r2 = LazyRule()
    print(r1.rules_filename)  # class property
    print(r2.rules_filename)  # class property
    r2.rules_filename = "r2-override.txt" # instance property
    print(r2.rules_filename)  # changed
    print(r1.rules_filename)  # not changed
    print(r2.__class__.rules_filename) # class<LazyRule>'s property
    r2.__class__.rules_filename = 'papayawhip.txt'  # change class's property
    print(r1.rules_filename)  # papayawhip.txt (affected)
    print(r2.rules_filename)  # r2-override.txt(not affected)