class Solution:
    """
    This class provides methods for finding the missing number in an array.
    """
    def missing_number(self,array,n):
        """
        Finds the missing number in the given array.

        Args:
            array (list): The input array.
            n (int): The length of the array.

        Returns:
            int: The missing number in the array.
        """
        actual_list = list(range(1, n+1))
        return list(set(actual_list) - set(array))[0]

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missing_number(a,n)
    print(s)