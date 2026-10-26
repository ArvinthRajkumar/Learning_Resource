import heapq

def meeting_rooms_ii(intervals):
    rooms = []                              # end times of rooms in use
    for start, end in sorted(intervals):
        if rooms and rooms[0] <= start:
            heapq.heapreplace(rooms, end)   # reuse the room that frees first
        else:
            heapq.heappush(rooms, end)
    return len(rooms)
