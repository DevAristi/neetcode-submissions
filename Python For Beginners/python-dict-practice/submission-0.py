from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    final_dict={}
    for i in word:
        if i in final_dict:
            final_dict[i]+=1
        else:
            final_dict[i]=1
    return final_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
