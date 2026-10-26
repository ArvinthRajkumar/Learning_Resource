def reverse_list(head):
    vals = to_list(head)[::-1]
    dummy = tail = ListNode()
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
