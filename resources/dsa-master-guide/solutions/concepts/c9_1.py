def delete_value(head, val):
    dummy = ListNode(0, head)          # dummy handles deleting the head
    prev, cur = dummy, head
    while cur:
        if cur.val == val:
            prev.next = cur.next       # unlink cur
            break
        prev, cur = cur, cur.next
    return dummy.next
