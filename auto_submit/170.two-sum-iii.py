from collections import Counter
class TwoSum:
    def __init__(self):
        self.nums = Counter()

    def add(self, number):
        """
        @param number: An integer
        @return: nothing
        """
        self.nums[number] += 1

    def find(self, value):
        """
        @param value: An integer
        @return: Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.nums:
            count = self.nums[value - n] 
            print n, value - n, count
            if n == value - n and count >= 2 or n != value - n and count >= 1:
                return True
        return False

class Solution:
    def test(self):
        twosum = TwoSum()
        twosum.add(2)
        twosum.add(3)
        print twosum.find(4)
