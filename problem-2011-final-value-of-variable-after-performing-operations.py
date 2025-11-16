from typing import List

def delta(op):
    if '+' in op:
        return +1
    else:
        return -1

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(delta(op) for op in operations)
