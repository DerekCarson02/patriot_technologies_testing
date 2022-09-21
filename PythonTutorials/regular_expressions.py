import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] / \ | ( )

derekcarson.com

454-403-5544
101-302-2003
101*302*2003
900-303-2003
800-302-2003

Mr. Carson
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

# raw strings are strings that don't handle backslashes in any special way

print('\t Tab')
print(r'\t Tab')

# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[a-zA-Z0-9]')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

epattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z-]+\.(com|edu|net)')
ematches = epattern.finditer(emails)

upattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
umatches = upattern.finditer(urls)

for match in matches:
    print(match)

for match in ematches:
    print(match)

for match in umatches:
    print(match)
