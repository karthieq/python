import re

# Regexs:
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

# #### Sample Regexs ####
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

text_to_search = '''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T'''

pattern = re.compile(r'abc')
for match in pattern.finditer(text_to_search):
    print(match)

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(matches)
pattern = re.compile(r'end$')
matches = pattern.search(sentence)
print(matches)

urls = '''https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

for match in pattern.finditer(urls):
    print(match.group(2))


# st = "aaa@gmail.com bbb@amazon.com ccc@walmart.com"
# print(re.sub('([a-z]*)@', '\1 19-@', st))
name = "scaqai11adm08.us.oracle.com"
print(re.sub(r'\w+(\.\w*)*', 'HOSTNAME', name))

emurl = "https://scaqai11adm08.us.oracle.com:1831/emd/main/"
print(re.sub(r'\w+(\.\w*)*:\d+', 'HOSTNAME:PORT', emurl))

cdate = "2021-06-21 15:02:55.0"
print(re.sub(r'\d+(-\d+){2}\s\d+(:\d+){2}\.\d', 'DATE', cdate))
