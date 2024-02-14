"""
Module-level docstring: Description of the purpose of the module.
"""
def is_subset( a1, a2, n, m):
    """
    Check if a2 is a subset of a1.

    Parameters:
        a1 (list): The first list.
        a2 (list): The second list.
        n (int): The length of a1.
        m (int): The length of a2.

    Returns:
        bool: True if a2 is a subset of a1, False otherwise.
    """
    freq_a1 = {}
    freq_a2 = {}

    for num in a1:
        freq_a1[num] = freq_a1.get(num, 0) + 1

    for num in a2:
        freq_a2[num] = freq_a2.get(num, 0) + 1

    for num, count in freq_a2.items():
        if num not in freq_a1 or freq_a1[num] < count:
            return "No"
    return "Yes"

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    """
    This function takes input, processes it, and prints the result.

    Returns:
        None
    """

    t = int(input())

    while t > 0:
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]

        print(is_subset( a1, a2, n, m))

        t -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends