# -*- coding : utf-8 -*-

'a test module'

__author__ = 'Xiang Su'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
        
if __name__ == '__main__':
    print('This program is being run by itself.')
    test()
else:
    print('I am being imported from another module.')
    
# When the Python interpreter reads a source file, it executes all of the code found in it.
# Before executing the code, it will define a few special variables. For example, 
# if the Python interpreter is running that module (the source file) as the main program, 
# it sets the special __name__ variable to have a value "__main__". If this file is being 
# imported from another module, __name__ will be set to the module's name.

# Therefore, this 'if test' allows a module to execute some extra code 
# when running it from the command line. The most common usage is to run the test code(运行测试).
