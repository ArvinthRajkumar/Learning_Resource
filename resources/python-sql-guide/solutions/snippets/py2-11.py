import math
import json as j
from collections import Counter
from os.path import join, basename as bn
print(math.sqrt(16), j.dumps([1]), Counter("aab"), bn(join("a", "b.txt")))
import sys
print("math" in sys.modules, type(math).__name__)
