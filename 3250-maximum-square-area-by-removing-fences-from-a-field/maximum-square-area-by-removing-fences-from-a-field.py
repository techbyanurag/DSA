class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        def get_all_distances(fence_positions: list[int], field_size: int) -> set[int]:
            all_positions = sorted(fence_positions + [1, field_size])
            distances = set()
            for i in range(len(all_positions)):
                for j in range(i + 1, len(all_positions)):
                    distances.add(all_positions[j] - all_positions[i])
            return distances

        MOD = 10**9 + 7
        horizontal_distances = get_all_distances(hFences, m)
        vertical_distances = get_all_distances(vFences, n)
        common_distances = horizontal_distances & vertical_distances
        max_side_length = max(common_distances, default=0)

        return (max_side_length ** 2) % MOD if max_side_length > 0 else -1
