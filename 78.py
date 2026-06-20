
import math
import os
import random
import re
import sys


from collections import Counter
if __name__ == '__main__':
    s = input()
    freq = Counter(s)
    sorted_items = sorted(freq.items(),key = lambda x: (-x[1],x[0]))
    for char,count in sorted_items[:3]:
        print(char,count)