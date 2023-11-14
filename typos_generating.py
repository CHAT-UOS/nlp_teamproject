import random
from unicode import join_jamos
from jamo import h2j, j2hcj
from typos_dict import typos_dict


def typos_generator(text):
    jamo_text = j2hcj(h2j(text))
    print("자모 분리: ", jamo_text)
    typos_str = ''
    for i, jamo in enumerate(jamo_text):
        for key, value in typos_dict.items():
            if jamo == key:
                select = random.random()
                probability = 0
                for char, i in value:
                    probability += i
                    if select <= probability:
                        typos_str = typos_str + char
                        break
    return join_jamos(typos_str)
