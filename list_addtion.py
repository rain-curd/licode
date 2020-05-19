class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = int(''.join([str(i) for i in l1][::-1]))
        l2 = int(''.join([str(j) for j in l2][::-1]))
        return l1 + l2
