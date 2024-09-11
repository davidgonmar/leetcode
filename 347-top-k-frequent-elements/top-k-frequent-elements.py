class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        return [i for i, n in sorted(count.items(), key=lambda item: item[1])[-k:]]
