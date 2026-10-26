def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next      # 1. remember the rest
        cur.next = prev     # 2. flip the arrow
        prev = cur          # 3. move prev forward
        cur = nxt           # 4. move cur forward
    return prev
