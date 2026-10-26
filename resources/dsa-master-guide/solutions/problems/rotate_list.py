def rotate_list(head, k):
    if not head or not head.next or k == 0:
        return head
    n, tail = 1, head
    while tail.next:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head                      # make a ring
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next
    new_head, new_tail.next = new_tail.next, None
    return new_head
