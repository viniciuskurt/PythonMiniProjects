# Wordlist creation project that can be used to test authentication and confidentiality of systems.

import itertools

string = input('String to be exchanged: ')

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
