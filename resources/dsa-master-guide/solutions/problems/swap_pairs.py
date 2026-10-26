def swap_pairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        a, b = prev.next, prev.next.next
        a.next, b.next, prev.next = b.next, a, b
        prev = a
    return dummy.next
