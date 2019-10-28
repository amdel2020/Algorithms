from collections import namedtuple, defaultdict

Event = namedtuple('event', ['start', 'end'])

event1 = Event(start = 1, end = 5)
event2 = Event(start = 6, end = 10)
event3 = Event(start = 11, end = 13)
event4 = Event(start = 14, end = 15)
event5 = Event(start = 2, end = 7)
event6 = Event(start = 8, end = 9)
event7 = Event(start = 12, end = 15)
event8 = Event(start = 4, end = 5)
event9 = Event(start = 9, end = 17)

events = [event1, event2, event3, event4, event5, event6, event7, event8, event9]

def max_concurrent_events(events):

    start = []
    end = []
    l, h = float('inf'), 0
    for e in events:
        start.append(e.start)
        end.append(e.end)
    
    start.sort()
    end.sort()

    i, j, c, r, l = 0, 0, 0, 0, len(start)
    while i < l:
        if start[i] < end[j]:
            c += 1
            i += 1
        elif start[i] > end[j]:
            c -= 1
            j += 1
        else:
            i += 1
            j += 1
        r = max(r, c)
    
    return r

print(max_concurrent_events(events))