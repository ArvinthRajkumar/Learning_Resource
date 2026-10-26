def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next             # 1 step
        fast = fast.next.next        # 2 steps
        if slow is fast:             # met inside the cycle
            return True
    return False
