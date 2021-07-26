#File hidden

import ctypes

atribute_hidden = 0x02

#variable back receives parameters and points to file or folder to be hidden
back = ctypes.windll.kernel32.SetFileAttributesW('06_ex_file.txt', atribute_hidden)

if back:
    print('File was hidden!')
else:
    print('File was not hidden!')