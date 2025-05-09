class Solution:
    def minInsertions(self, s: str) -> int:
        # Use a dictionary to memoize results of subproblems
        d = {}

        # Recursive helper function to find min insertions needed between indices i and j
        def rec(i, j):
            # Base case: if the pointers have met or crossed, no insertion is needed
            if i >= j:
                return 0
            # If result is already computed, return it
            if (i, j) in d:
                return d[(i, j)]
            # If characters match, move both pointers inward
            if s[i] == s[j]:
                d[(i, j)] = rec(i + 1, j - 1)
            else:
                # If not, try inserting at either end and take the min
                d[(i, j)] = 1 + min(rec(i + 1, j), rec(i, j - 1))
            return d[(i, j)]

        # Call the recursive function on the entire string
        return rec(0, len(s) - 1)

            
        