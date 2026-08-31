from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_dict = dict(sorted(Counter(nums).items(), key=lambda item: item[1]))
        return(list(sorted_dict.keys()) [-k:])
