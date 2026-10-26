def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head                 # phase 2
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow.val
    return None
