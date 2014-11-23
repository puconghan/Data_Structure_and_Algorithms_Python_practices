'''
Implementation for regular expression pattern matching for '.' and '*'
'''

def pattern_matching(string, pattern):
    if len(pattern) == 0:
        return len(string) == 0
    if len(pattern) == 1:
        if pattern[0] != '.':
            return (string[0] == pattern[0] and len(string) == 1)
        else:
            return True
    else:
        if pattern[1] == '*':
            if string[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                pattern = pattern[2:]
                while len(string) >= 2 and string[0] == string[1]:
                    string = string[1:]
                string = string[1:]
                return pattern_matching(string, pattern)
        else:
            if string[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                return pattern_matching(string[1:], pattern[1:])

print pattern_matching('a', 'a'), True
print pattern_matching('a', 'b'), False
print pattern_matching('aa', 'aa'), True
print pattern_matching('aa', 'ab'), False
print pattern_matching('aa', 'a.'), True
print pattern_matching('aa', '.*'), True
print pattern_matching('aaa', 'a*'), True
print pattern_matching('aaa', '.*'), True
print pattern_matching('aabbcc', 'a*c*'), False
print pattern_matching('abc', 'a*b*c*'), True

