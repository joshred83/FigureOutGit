# Write a function that uses regular expressions to make sure the password string it
# is passed is strong. A strong password is defined as one that is at least eight
# characters long, contains both uppercase and lowercase characters, and has at
# least one digit. You may need to test the string against multiple regex patterns to
# validate its strength.

import re


def pw_length(pw):
    len_regex = re.compile(r'(\S){8,}')
    return len_regex.search(pw) is not None


def pw_upper_lower(pw):
    has_upper_regex = re.compile(r'[A-Z]+')
    has_lower_regex = re.compile(r'[a-z]+')
    return (has_upper_regex.search(pw) is not None
            and has_lower_regex.search(pw) is not None)


def pw_has_a_num(pw):
    has_num_regex = re.compile(r'(\d)+')
    return has_num_regex.search(pw) is not None


def main():
    password = input("Enter the password to be tested: ")

    length_ok = pw_length(password)

    case_ok = pw_upper_lower(password)

    number_ok = pw_has_a_num(password)

    if not length_ok:
        print('The password must be at least eight characters.')

    if not case_ok:
        print('The password must include lower and uppercase characters. ')

    if not number_ok:
        print('The password must include at least one number.')

    if length_ok and case_ok and number_ok:
        print('Acceptable password.')


if __name__ == '__main__':
    main()
