def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next      # remember the rest
        cur.next = prev     # flip the arrow
        prev = cur          # advance both pointers
        cur = nxt
    return prev
