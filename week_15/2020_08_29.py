# 445. Add Two Numbers II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        stack1 = []
        stack2 = []
        
        curr = l1
        while curr is not None:
            stack1.append(curr.val)
            curr = curr.next
        
        curr = l2
        while curr is not None:
            stack2.append(curr.val)
            curr = curr.next
        
        dummy = None
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            total = carry
            if len(stack1) > 0:
                total += stack1.pop()
            if len(stack2) > 0:
                total += stack2.pop()
            
            carry = total // 10
            total = total % 10
            
            dummy = ListNode(total, dummy)
        
        return dummy if carry == 0 else ListNode(carry, dummy)

# 450. Delete Node in a BST
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        
        def del_root(root):
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                curr = root.left
                if curr.right is None:
                    curr.right = root.right
                    return curr
                while curr.right is not None:
                    prev = curr
                    curr = curr.right
                prev.right = curr.left
                return TreeNode(curr.val, root.left, root.right)
        
        if root.val == key:
            return del_root(root)
        else:
            stack = [(root, root.left)] if key < root.val else [(root, root.right)]
            while len(stack) > 0:
                prev, curr = stack.pop()
                if curr is not None:
                    if curr.val == key:
                        if key < prev.val:
                            prev.left = del_root(curr)
                        else:
                            prev.right = del_root(curr)
                        break
                    elif curr.val > key:
                        stack.append((curr, curr.left))
                    else:
                        stack.append((curr, curr.right))
            return root

