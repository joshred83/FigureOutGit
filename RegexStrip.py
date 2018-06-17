# Regex version of strip()
# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and end
# of the string. Otherwise, the characters specified in the second argument to
# the function will be removed from the string.

import re


def reg_ex_strip(string, remove=None):
    if remove is None:
        starts_with = re.compile(r'^\s+')
        ends_with = re.compile(r'\s+$')
        string = starts_with.sub('',string)
        string = ends_with.sub('', string)
        return string

    else:
        starts_with = "^" + remove + "+"
        starts_with = re.compile(starts_with)
        string = starts_with.sub('', string)
        ends_with = remove + "+$"
        ends_with = re.compile(ends_with)
        string = ends_with.sub('', string)
        return string


def main():
    the_string = '   this be the string   '

    modified_string = reg_ex_strip(the_string)
    print(modified_string)

    the_string = 'aaaaathis be the other stringaaaaa'
    modified_string = reg_ex_strip(the_string, remove='a')
    print(modified_string)


if __name__ == '__main__':
    main()
