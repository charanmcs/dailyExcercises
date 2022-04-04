from importlib.resources import contents
import sys
import pandas as pd
import numpy as np
import regex as re
f=open(sys.argv[1],'r',encoding='utf-8')
contents = f.read()
pattern1 = r"[£₹$][0-9]{1,}"
pattern2 = re.compile(r"(([0-1]\d\/[0-3]\d\/|([0-3]\d\/[0-1]\d\/))\d\d(\d{2})?)")
pattern3 = re.compile("(\d*(1st|2nd|3rd|[04-9]th))|[a-zA-Z]*(first|eleventh|second|twe(l(ve|th)|ntyth)|thir(teenth|d|tyth)|four((teen)?th|tyth)|fif((teen)?th|tyth)|six((teen)?th|tyth)|seven((teen)?th|tyth)|eigh((teen)?th|tyth)|nine((teen)?th|tyth)|tenth)")
pattern4 = r"\b[aeiouAEIOU][a-zA-Z]{3}\b"
print("Currencie Matches : ",end="")
for match in re.findall(pattern1,contents):
    print(match,end=" ")
print("\nDate Matches : ",end="")
for match in re.finditer(pattern2,contents):
    print(match.group(0),end=" ")
print("\nOrder or Cardinalities Matches : ",end="")
for match in re.finditer(pattern3,contents):
    print(match.group(0),end=" ")
print("\nFour letter words begining with vowels : ",end="")
for match in re.findall(pattern4,contents):
    print(match,end=" ")
f.close()