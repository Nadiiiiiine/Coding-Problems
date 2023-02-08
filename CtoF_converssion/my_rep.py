import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

d = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if d % 2 != 0:
   dc = (d-32) * (5/9)
   print(round(dc))
else:
    df = (9/5 * d) + 32
    print(round(df))

