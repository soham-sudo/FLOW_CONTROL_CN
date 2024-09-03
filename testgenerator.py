

import string
import random
import re

n = 7 * (32 * 13)

res = ''.join(random.choice('01') for _ in range(n))
file = open("data.txt", "w")
file.write(res)
file.close()
