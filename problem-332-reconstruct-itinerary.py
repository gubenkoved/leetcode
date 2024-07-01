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
                return path

            for next_ticket in sorted(available[cur]):
                if available[cur][next_ticket] == 0:
                    continue
                available[cur][next_ticket] -= 1
                next_dest = next_ticket[1]
                path.append(next_dest)
                sub_result = find(next_dest, path, available)
                if sub_result is not None:
                    return sub_result
                path.pop(-1)
                available[cur][next_ticket] += 1

        return find('JFK', ['JFK'], tickets_by_source)


case_idx = 0


def visualize(tickets):
    import pyvis
    global case_idx
    case_idx += 1
    g = pyvis.network.Network(directed=True, height='1000px', width='100%')
    nodes = set()
    for source, dest in tickets:
        if source not in nodes:
            g.add_node(source)
            nodes.add(source)
        if dest not in nodes:
            g.add_node(dest)
            nodes.add(dest)
        g.add_edge(source, dest)
    # g.barnes_hut()
    g.force_atlas_2based()
    g.toggle_physics(False)
    g.write_html('problem-332-case-%s.html' % case_idx, open_browser=False)


if __name__ == '__main__':
    x = Solution()

    def case(tickets):
        visualize(tickets)
        print(x.findItinerary(tickets))

    case([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    case([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"],
          ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]])
    # limits exceeded
    case([["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
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
         ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]])
