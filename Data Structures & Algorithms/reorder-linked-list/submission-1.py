# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Brute Force Approach
        # if not head:
        #     return
        # nodes = []
        # curr = head

        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next        

        # i, j = 0, len(nodes)-1
        # while i<j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i>=j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j -= 1
        # nodes[i].next = None

        #Recursion Approach

        def rec(root:ListNode, cur:ListNode)-> ListNode:
            if not cur:
                return root
            
            root = rec(root, cur.next)
            if not root:
                return None
            
            tmp = None
            if root == cur or root.next==cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp
        head = rec(head, head.next)

