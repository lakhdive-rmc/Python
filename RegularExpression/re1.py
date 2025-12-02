# program to whether string start with letter 'a'
# program to whether string start with letter 'a' and ends with 'b'

import re
print("All string start with a : ")
pattern = r"^a"

texts = ["ab", "acb", "appleb", "axb", "abc", "ba"]

for t in texts:
    if re.match(pattern, t):
        print(t, "→ MATCH")
    else:
        print(t, "→ NO MATCH")


print("All string start with a and ends with b : ")
pattern = r"^a.*b$"

texts = ["ab", "acb", "appleb", "axb", "abc", "ba"]

for t in texts:
    if re.match(pattern, t):
        print(t, "→ MATCH")
    else:
        print(t, "→ NO MATCH")
