def delete_duplicates_list(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next      # unlink the duplicate
        else:
            cur = cur.next
    return head
