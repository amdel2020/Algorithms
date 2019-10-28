from collections import defaultdict, Counter

para = "My paramount object in this struggle is to save the Union and is not either to save or to destroy slavery If I could save the Union without freeing any slave I would do it and if I could save it by freeing all the slaves I would do it and if I could save it by freeing some and leaving others alone I would also do that".lower().split()
keywords = ["union", "save"]


def smallest_covering_subarray(paragraph, keywords):
    key_table = Counter(keywords)
    idx = 0

    for i, s in enumerate(paragraph):
        if s in keywords:
            key_table[s] -= 1


print(smallest_covering_subarray(para, keywords))
