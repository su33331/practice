## ２.  Add Two Numbers
### 24問目
### [問題リンク](https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=ryq3bf2c)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#1st:書ききれずに解答を見る
#2nd:13min
#3rd:4min
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head
        carry = 0

        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10

            next_node = ListNode(total % 10)
            tail.next = next_node
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next

### 参考を見て書いた他方法
#再帰を使う方法
#dummy_headを使わない方法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        def add_two_num_helper(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return None

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10

            new_node = ListNode(total % 10)
            sum_node_head = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum_node_head.next = add_two_num_helper(l1, l2, carry)
            return sum_node_head
        return add_two_num_helper(l1, l2, carry)

'''
参考にしたもの
* https://github.com/cheeseNA/leetcode/pull/2
→ 再帰を使った方法
→ python3のintはdoubleに相当し、その上限はメモリに依存する　→
[python docのint概要](https://docs.python.org/ja/3/library/functions.html#int)
→ int()の第二引数で基数を指定することで、異なる基数の値も整数値への変換もできる。文字列も可能。
→ 逆に2,8,16進数への変換は bin(), oct(), hex()
'''
