"""
Topic: Arrays – Fundamentals

Purpose:
- Understand how arrays work internally
- Build intuition using basic operations & logic
- This file may contain simple problems that strengthen fundamentals

Note:
- No advanced interview patterns here
- Focus is on clarity, not cleverness
"""


class ArrayFundamentals:
    """
    This class contains fundamental array operations and basic logic.
    """

    # --------------------------------------------------
    # 1. Traversal
    # --------------------------------------------------
    def traverse(self, arr: list[int]) -> None:
        """
        Concept: Traversal
        """
        for ele in arr:
            print(ele)

    def traverse_with_index(self, arr: list[int]) -> None:
        """
        Concept: Index vs Value
        """
        for idx, val in enumerate(arr):
            print(f"Index {idx} -> Value {val}")

    def reverse_traversal(self, arr: list[int]) -> None:
        """
        Concept: Reverse traversal
        """
        for idx in range(len(arr) - 1, -1, -1):
            print(arr[idx], end=" ")
        print()

    # --------------------------------------------------
    # 2. Basic Operations
    # --------------------------------------------------
    def array_length(self, arr: list[int]) -> int:
        return len(arr)

    def sum_of_elements(self, arr: list[int]) -> int:
        total = 0
        for ele in arr:
            total += ele
        return total

    def average_of_elements(self, arr: list[int]) -> float:
        return self.sum_of_elements(arr) / len(arr)

    # --------------------------------------------------
    # 3. Maximum & Minimum
    # --------------------------------------------------
    def find_max(self, arr: list[int]) -> int:
        """
        Concept: Maximum element
        """
        max_val = arr[0]
        for ele in arr:
            if ele > max_val:
                max_val = ele
        return max_val

    def find_min(self, arr: list[int]) -> int:
        """
        Concept: Minimum element
        """
        min_val = arr[0]
        for ele in arr:
            if ele < min_val:
                min_val = ele
        return min_val

    # --------------------------------------------------
    # 4. Reverse Array (Two Pointer Intro)
    # --------------------------------------------------
    def reverse_array(self, arr: list[int]) -> list[int]:
        """
        Concept: Reverse array using two pointers
        """
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    # --------------------------------------------------
    # 5. Searching & Counting
    # --------------------------------------------------
    def linear_search(self, arr: list[int], key: int) -> int:
        """
        Concept: Linear search
        """
        for idx in range(len(arr)):
            if arr[idx] == key:
                return idx
        return -1

    def count_occurrence(self, arr: list[int], num: int) -> int:
        """
        Concept: Count frequency of an element
        """
        count = 0
        for ele in arr:
            if ele == num:
                count += 1
        return count

    def first_occurrence(self, arr: list[int], num: int) -> int:
        """
        Concept: First occurrence (left to right)
        """
        for idx in range(len(arr)):
            if arr[idx] == num:
                return idx
        return -1

    def last_occurrence(self, arr: list[int], num: int) -> int:
        """
        Concept: Last occurrence (right to left)
        """
        for idx in range(len(arr) - 1, -1, -1):
            if arr[idx] == num:
                return idx
        return -1

    # --------------------------------------------------
    # 6. Uniqueness Check (Brute Force)
    # --------------------------------------------------
    def is_all_unique(self, arr: list[int]) -> bool:
        """
        Concept: Check if all elements are unique
        Time Complexity: O(n^2)
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return False
        return True


# --------------------------------------------------
# Testing Fundamentals
# --------------------------------------------------
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 5]

    obj = ArrayFundamentals()

    print("Traversal:")
    obj.traverse(arr)

    print("\nTraversal with index:")
    obj.traverse_with_index(arr)

    print("\nReverse traversal:")
    obj.reverse_traversal(arr)

    print("\nLength:", obj.array_length(arr))
    print("Sum:", obj.sum_of_elements(arr))
    print("Average:", obj.average_of_elements(arr))
    print("Max:", obj.find_max(arr))
    print("Min:", obj.find_min(arr))
    print("Reversed:", obj.reverse_array(arr.copy()))

    print("\nLinear search (2):", obj.linear_search(arr, 2))
    print("Count of 2:", obj.count_occurrence(arr, 2))
    print("First occurrence of 2:", obj.first_occurrence(arr, 2))
    print("Last occurrence of 2:", obj.last_occurrence(arr, 2))
    print("All unique:", obj.is_all_unique(arr))
