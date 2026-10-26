def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next          # fewer than k nodes left
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:       # reverse this block
            cur.next, prev, cur = prev, cur, cur.next
        tail = group_prev.next
        group_prev.next = kth
        group_prev = tail
