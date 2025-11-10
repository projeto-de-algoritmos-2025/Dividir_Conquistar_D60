from typing import List

class Solution:
	def reversePairs(self, nums: List[int]) -> int:
		# O(n log n) com Fenwick Tree + compressão de coordenadas (sem mergesort)
		n = len(nums)
		if n <= 1:
			return 0

		# Compressão de coordenadas para valores de nums e 2*nums
		all_vals = list(set(nums + [2 * v for v in nums]))
		all_vals.sort()
		rank = {v: i + 1 for i, v in enumerate(all_vals)}

		class BIT:
			def __init__(self, size: int) -> None:
				self.n = size
				self.ft = [0] * (size + 1)
			def update(self, i: int, delta: int) -> None:
				while i <= self.n:
					self.ft[i] += delta
					i += i & -i
			def query(self, i: int) -> int:
				s = 0
				while i > 0:
					s += self.ft[i]
					i -= i & -i
				return s

		bit = BIT(len(all_vals))
		result = 0
		seen = 0
		for v in nums:
			# pares com anterior > 2*v
			i2 = rank[2 * v]
			result += seen - bit.query(i2)
			# adiciona v
			bit.update(rank[v], 1)
			seen += 1
		return result