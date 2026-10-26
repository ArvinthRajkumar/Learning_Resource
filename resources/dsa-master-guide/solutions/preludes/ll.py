class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "Node(%r)" % (self.val,)

def build(values, cycle_pos=-1):
    """Build a linked list from a Python list (cycle_pos links the tail back to that index)."""
    dummy = ListNode()
    cur, nodes = dummy, []
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    if 0 <= cycle_pos < len(nodes):
        cur.next = nodes[cycle_pos]
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
