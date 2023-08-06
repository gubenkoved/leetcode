from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depends = defaultdict(list)  # course -> prerequisites

        for course, depends_on in prerequisites:
            depends[course].append(depends_on)

        learned = set()
        visited = set()

        def learn(course) -> bool:   # returns True if cycle is found
            if course in visited:
                return True

            visited.add(course)

            for dependency in depends.get(course, []):
                if dependency in learned:
                    continue

                cycle = learn(dependency)

                # stop if we detected cycle
                if cycle:
                    return True

            learned.add(course)
            return False

        for course in range(numCourses):
            if course in learned:
                continue

            cycle_found = learn(course)

            if cycle_found:
                return False

        return True


if __name__ == '__main__':
    x = Solution()
    print(x.canFinish(2, [[0, 1]]))
