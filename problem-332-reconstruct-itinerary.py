from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_by_source = defaultdict(lambda: defaultdict(int))
        all_possible = set()

        for source, dest in tickets:
            tickets_by_source[source][(source, dest)] += 1
            all_possible.add(source)
            all_possible.add(dest)

        results = []

        def find(cur, path, available):
            if len(path) == len(tickets) + 1:
                results.append(tuple(path))

            for next_ticket in list(available[cur]):
                if available[cur][next_ticket] == 0:
                    continue
                available[cur][next_ticket] -= 1
                next_dest = next_ticket[1]
                path.append(next_dest)
                find(next_dest, path, available)
                path.pop(-1)
                available[cur][next_ticket] += 1

        # for start in all_possible:
        #     find(start, [start], tickets_by_source)

        find('JFK', ['JFK'], tickets_by_source)

        return list(min(results))


if __name__ == '__main__':
    x = Solution()
    # print(x.findItinerary(
    #     [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # print(x.findItinerary(
    #     [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"],
    #      ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]
    # ))
    print(x.findItinerary(
        [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
         ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"],
         ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"],
         ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
         ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"],
         ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
         ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"],
         ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
         ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"],
         ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"],
         ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
         ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
         ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"],
         ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"],
         ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]]))
