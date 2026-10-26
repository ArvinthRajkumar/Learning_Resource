def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    prev, cur = None, slow.next
    slow.next = None                       # split into two lists
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    first, second = head, prev
    while second:
        n1, n2 = first.next, second.next
        first.next, second.next = second, n1
        first, second = n1, n2
