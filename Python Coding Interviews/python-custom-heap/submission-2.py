import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []

    for num in nums:
        heapq.heappush(heap, (-num, num))
        
    res = []
    while heap:
        priority, original_num = heapq.heappop(heap)
        res.append(original_num)
        
    return res



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
