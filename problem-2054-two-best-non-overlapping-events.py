from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sub_events = []

        for start, end, value in events:
            # 0 start, 1 end so that we process all start before all end
            # to handle non-intersection condition easily
            sub_events.append((start, 0,  value))
            sub_events.append((end, 1,  value))

        # sort these "sub events"
        sub_events.sort()

        result = 0
        max_value_finished = 0
        for t, type, value in sub_events:
            if type == 0:
                result = max(result, max_value_finished + value)
            elif type == 1:
                max_value_finished = max(max_value_finished, value)
        return result
