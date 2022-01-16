from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        city_to_arrive = dict()
        for path in paths:
            city_a, city_b = path
            city_to_arrive[city_a], city_to_arrive[city_b] = city_to_arrive.get(city_a, 0) + 1, city_to_arrive.get(city_b, 0)
        for key in city_to_arrive.keys():
            if city_to_arrive[key] == 0:
                return key


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
ret = Solution().destCity(paths)
assert ret == "Sao Paulo"

# Runtime: 48 ms, faster than 94.96% of Python3 online submissions for Destination City.
# Memory Usage: 14.2 MB, less than 72.40% of Python3 online submissions for Destination City.