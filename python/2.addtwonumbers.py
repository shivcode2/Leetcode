from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convertToNumber(self, currlinklist):
        current_node = currlinklist
        reverse_digits_in_list = []
        while current_node:
            reverse_digits_in_list.append(current_node.val)
            current_node = current_node.next
        
        normal_digits_in_list = reverse_digits_in_list[::-1]  # Reverse the list to get the correct order
        single_number = int(''.join(map(str, normal_digits_in_list)))
        
        return single_number
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_a = self.convertToNumber(l1)
        number_b = self.convertToNumber(l2)

        number_add = number_a + number_b

        digits_add = list(map(int, str(number_add)))
        reverse_digits_add = digits_add[::-1]  # Reverse the digits to store them in reverse order in the linked list

        head = ListNode(reverse_digits_add[0])
        current = head

        for i in range(1, len(reverse_digits_add)):
            new_node = ListNode(reverse_digits_add[i])
            current.next = new_node
            current = current.next

        return head

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Example usage:
l1 = create_linked_list([2, 4, 3])  # Represents the number 342
l2 = create_linked_list([5, 6, 4])  # Represents the number 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should represent the number 807 (7 -> 0 -> 8)
