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
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            next_val = total % 10
            carry = total // 10

            next_node = ListNode(next_val)
            tail.next = next_node
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        l3 = dummyHead.next
        return l3

### 参考を見て書いた他方法
#再帰を使う方法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        l3 = dummyHead
        carry = 0

        def add_two_num_helper(l1, l2, carry, l3):
            if l1 is None and l2 is None and carry == 0:
                return None
            else:
                l1_val = l1.val if l1 else 0
                l2_val = l2.val if l2 else 0
                total = l1_val + l2_val + carry
                next_val = total % 10
                carry = total // 10

                next_node = ListNode(next_val)
                l3.next = next_node
                l3 = l3.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                l3.next = add_two_num_helper(l1, l2, carry, l3)
                return l3
        l3 = add_two_num_helper(l1, l2, carry, l3)
        result = dummyHead.next
        return result

'''
参考にしたもの
* https://github.com/cheeseNA/leetcode/pull/2
→ 再帰を使った方法
→ python3のintはdoubleに相当し、その上限はメモリに依存する　→
[python docのint概要](https://docs.python.org/ja/3/library/functions.html#int)
→ int()の第二引数で基数を指定することで、異なる基数の値も整数値への変換もできる。文字列も可能。
→ 逆に2,8,16進数への変換は bin(), oct(), hex()
'''
