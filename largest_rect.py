def largest_rect(h):
    max_area = 0
    l = len(h)

    for i in range(h):
        for j in range(i, h):
            area = min(h[i:j]) * (j-i+1)
            max_area = max(max_area, area)

    return max_area