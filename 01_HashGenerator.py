#This is a basic hash generator project

import hashlib

string = input('Please, enter the text to generate the string: ')

menu = int(input(''' ### MENU - CHOOSE THE TYPE OF HASH:
                        1) MD5
                        2) SHA1
                        3) SHA256
                        4) SHA512
            ENTER THE NUMBER OF THE HASH TO BE GENERATED: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print('The MD5 hash of the string: ', string, ' is: ', result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print('The SHA1 hash of the string: ', string, ' is: ', result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print('The SHA256 hash of the string: ', string, ' is: ', result.hexdigest())
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print('The SHA512 hash of the string: ', string, ' is: ', result.hexdigest())
else:
    print('Invalid!! Try Again')
