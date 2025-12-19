import collections
import heapq
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # we can basically build the graph and use Dijkstra to find all minimal times
        # it takes to get the secret;
        # meetings are edges in that graph, and we can traverse edge if time person
        # first knew the secret is <= time of the meeting

        # person -> list of meetings which is tuple of (time, person)
        meeting_map = collections.defaultdict(list)

        for p1, p2, t in meetings:
            meeting_map[p1].append((t, p2))
            meeting_map[p2].append((t, p1))

        knows_secret = set()

        # (t, person)
        heap = [
            (0, 0),
            (0, firstPerson)
        ]

        while heap:
            t, p = heapq.heappop(heap)

            if p in knows_secret:
                continue

            knows_secret.add(p)

            # find all the meetings he attends after
            for mt, p2 in meeting_map[p]:
                if mt < t:
                    continue
                heapq.heappush(heap, (mt, p2))

        return list(knows_secret)
