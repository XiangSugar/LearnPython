# -*- coding: utf-8 -*-
# The use of partial function

import functools
int2 = functools.partial(int, base=2)

print(int2('1000000'))
