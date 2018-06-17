import pyperclip, re


# phone Regex
phoneRegex = re.compile(r"""(
    (\d{3}|\(d{3}\))?     # area code (two variants, both optional)
    (s|-|\.)?             # separator (optional)
    (\d{3})               # first 3 digits (required)
    (\s|-|\.)             # separator (required)
    (\d{4})               # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
                        )""", re.VERBOSE)

emailRegex = re.compile(r'''(et
    [a-zA-Z0-9._%+-]+       # email name
    @                       # @
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,5})
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join(groups[1], groups[3], groups[5])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses.')
