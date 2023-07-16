import collections
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # basically the idea is to represent the task as a search of the shortest path in the graph
        # constructed with the nodes representing acquired skills (single number for the skill set)
        # and transitions are based on the individual skill sets
        # to do that we can simply traverse this imaginary graph in a BFS manner
        # keeping track the previous state to be able to reconstruct the path

        # convert people skillsets to numbers using bitmasks
        k = len(people)
        people_skillset = [0] * k  # people idx -> skillset mask

        for idx in range(k):
            mask = 0
            for skill in people[idx]:
                skill_index = req_skills.index(skill)
                mask += 2 ** skill_index
            people_skillset[idx] = mask

        # we need ALL the skills
        needed_skillset = (2 ** len(req_skills)) - 1

        visited = set()
        queue = collections.deque()

        queue.append(0)
        prev_map = {}  # state -> (prev_state, people_idx)

        while queue:
            skillset = queue.popleft()

            # finish condition
            if skillset == needed_skillset:
                break

            if skillset in visited:
                continue

            visited.add(skillset)

            # find next possible states
            for people_idx in range(k):
                new_skillset = people_skillset[people_idx] | skillset
                if new_skillset != skillset:
                    if new_skillset not in prev_map:
                        queue.append(new_skillset)
                        prev_map[new_skillset] = (skillset, people_idx)

        # backtrack to get the solution
        solution = []
        while skillset != 0:
            skillset, people_idx = prev_map[skillset]
            solution.append(people_idx)

        return solution


if __name__ == '__main__':
    x = Solution()
    print(x.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                   people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
    print(x.smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                   people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                           ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"],
                                           ["aws", "java"]]))
