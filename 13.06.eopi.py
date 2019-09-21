from collections import namedtuple, Counter

Subarray = namedtuple('Subarray', ('start', 'end'))

def smallest_subarray(para, keywords):
    keywords_to_cover = Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    para = para.split()

    for right, p in enumerate(para):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1
        
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = para[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] >= 0:
                    remaining_to_cover -= 1
            left += 1
    return result

para = "My paramaount object in this struggle is to Save the Union and is not either to save or to destroy slavery"
keywords = ["Union", "Save"]
print(smallest_subarray(para, keywords))