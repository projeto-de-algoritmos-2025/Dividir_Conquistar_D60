from typing import List, Tuple
import math

Point = Tuple[float, float]

def _dist(p: Point, q: Point) -> float:
	return math.hypot(p[0] - q[0], p[1] - q[1])

def closest_pair_of_points(points: List[Point]) -> float:
	if len(points) < 2:
		return float("inf")

	points_sorted_x = sorted(points, key=lambda p: (p[0], p[1]))
	points_sorted_y = sorted(points, key=lambda p: (p[1], p[0]))

	def _solve(px: List[Point], py: List[Point]) -> float:
		m = len(px)
		if m <= 3:
			best = float("inf")
			for i in range(m):
				for j in range(i + 1, m):
					best = min(best, _dist(px[i], px[j]))
			return best
		mid = m // 2
		mid_x = px[mid][0]
		left_x = px[:mid]
		right_x = px[mid:]

		left_set = set(left_x)
		left_y = [p for p in py if p in left_set]
		right_y = [p for p in py if p not in left_set]

		dl = _solve(left_x, left_y)
		dr = _solve(right_x, right_y)
		d = min(dl, dr)

		strip = [p for p in py if abs(p[0] - mid_x) < d]
		for i in range(len(strip)):
			for j in range(i + 1, min(i + 8, len(strip))):
				d = min(d, _dist(strip[i], strip[j]))
		return d

	return _solve(points_sorted_x, points_sorted_y)

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