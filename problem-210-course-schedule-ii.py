from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # looks like topological sort problem
        # course -> prerequsites list
        prerequisites_map = defaultdict(list)
        for course, pre_req_course in prerequisites:
            prerequisites_map[course].append(pre_req_course)

        schedule = []
        taken = set()
        parent_set = set()

        def take(course):
            # cycle found!
            if course in parent_set:
                return False

            parent_set.add(course)

            for prerequisite in prerequisites_map[course]:
                if prerequisite not in taken:
                    ok = take(prerequisite)
                    if not ok:
                        return False

            # all prerequisites are taken!
            taken.add(course)
            schedule.append(course)

            parent_set.discard(course)

            return True

        for course in range(numCourses):
            if course not in taken:
                parent_set = set()
                ok = take(course)
                if not ok:
                    return []

        return schedule


if __name__ == '__main__':
    x = Solution()
    print(x.findOrder(numCourses=2, prerequisites=[[1, 0]]))
    print(x.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(x.findOrder(numCourses=1, prerequisites=[]))
    print(x.findOrder(numCourses=3, prerequisites=[[0, 1], [1, 2]]))
    print(x.findOrder(numCourses=2, prerequisites=[[0, 1], [1, 0]]))
