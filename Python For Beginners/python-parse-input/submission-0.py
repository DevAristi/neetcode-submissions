from typing import List

def read_integers() -> List[int]:
    line=input()
    line1=line.split(",")
    final_line=[]
    for a in line1:
        final_line.append(int(a))
    return final_line


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
