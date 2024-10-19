# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convertToNumber(self, currlinklist):
        current_node = currlinklist
        reverse_digits_in_list = []
        while current_node:
            reverse_digits_in_list.append(current_node.val)
            current_node = current_node.next
        
        normal_digits_in_list = reverse_digits_in_list[ : : -1]
        single_number = int(''.join(map(str, normal_digits_in_list)))
        
        return single_number
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_a = self.convertToNumber(l1)
        number_b = self.convertToNumber(l2)

        number_add = number_a + number_b

        digits_add = list(map(int, str(number_add)))
        reverse_digits_add = digits_add[ : : -1]

        head = ListNode(reverse_digits_add[0])
        current = head

        for i in range(1, len(reverse_digits_add)):
            new_node = ListNode(reverse_digits_add[i])
            current.next = new_node
            current = current.next

        return head
