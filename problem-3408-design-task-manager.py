from typing import List
from sortedcontainers import SortedList


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # tasks as tuples of (priority, task_id)
        self.tasks = SortedList()
        # task id to (priority, user id)
        self.tasks_map = {}

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((priority, taskId))
        self.tasks_map[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        cur_priority, user_id = self.tasks_map[taskId]
        self.tasks.discard((cur_priority, taskId))
        self.tasks.add((newPriority, taskId))
        self.tasks_map[taskId] = (newPriority, user_id)

    def rmv(self, taskId: int) -> None:
        cur_priority, user_id = self.tasks_map[taskId]
        self.tasks.discard((cur_priority, taskId))

    def execTop(self) -> int:
        if not self.tasks:
            return -1

        _, task_id = self.tasks.pop(-1)
        _, user_id = self.tasks_map[task_id]
        return user_id
