from typing import List, Optional
import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.node_id = None
        self.position: int = -1
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

    def __repr__(self):
        return '<Node id=%d, value=%d, position=%d>' % (
            self.node_id, self.value, self.position)


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # count number of inversions
        # linked list of the numbers
        # heap of (pair_sum, pointer to where first node in pair?)

        # while number of inversions is bigger than zero
        #   find the pair with the smallest sum, find the nodes in the linked list
        #   merge nodes, update the head with pair sums and count of inversions

        # 5 4 3 1 9
        #     ^^^

        # when I remove a pair I also "invalidate" two more affected pairs
        # forever, so I need a way to mark these in the priority queue
        # pair can probably be identified by (node_id_1, node_id_2), and
        # when I merge the pair I create a new node ID, pop 1 pair,
        # invalidate 2 more pairs AND form 2 new pairs with a new node ID

        next_nid = 0
        nid_to_node = {}

        # (pair_sum, position, (nid1, nid2))
        pairs_heap = []

        inversions_count = 0

        prev_node = None
        for idx in range(len(nums)):
            node = Node(nums[idx])
            node.node_id = next_nid
            node.position = idx
            next_nid += 1
            nid_to_node[node.node_id] = node

            if prev_node:
                node.prev = prev_node
                prev_node.next = node

            if idx > 0:
                pair_sum = nums[idx] + nums[idx - 1]
                heapq.heappush(pairs_heap, (pair_sum, node.prev.position, (idx - 1, idx)))

            if idx > 0:
                if nums[idx] < nums[idx - 1]:
                    inversions_count += 1

            prev_node = node

        # set of (nid1, nid2) which were invalidated as a result of the merge op
        invalidated_pairs = set()

        def merge_nodes(node1, node2, new_node):
            nonlocal inversions_count

            # print('  merging %r + %r -> %r' % (node1, node2, new_node))

            # inversion within the pair is always eliminated if was present
            if node1.value > node2.value:
                inversions_count -= 1

            if node1.prev:
                if node1.prev.value > node1.value:
                    inversions_count -= 1

                if node1.prev.value > new_node.value:
                    inversions_count += 1

                node1.next = new_node
                new_node.prev = node1.prev

            if node2.next:
                if node2.value > node2.next.value:
                    inversions_count -= 1

                if new_node.value > node2.next.value:
                    inversions_count += 1

                node2.next.prev = new_node
                new_node.next = node2.next

        op_count = 0
        while inversions_count > 0:
            pair_sum, position, (nid1, nid2) = heapq.heappop(pairs_heap)

            if (nid1, nid2) in invalidated_pairs:
                continue

            node1: Node = nid_to_node[nid1]
            node2: Node = nid_to_node[nid2]

            # print('processing pair %r + %r' % (node1, node2))

            new_node = Node(node1.value + node2.value)
            new_node.node_id = next_nid
            next_nid += 1

            nid_to_node[new_node.node_id] = new_node

            if node1.prev:
                new_node.position = node1.prev.position + 1
                invalidated_pairs.add((node1.prev.node_id, node1.node_id))

                # add a new pair with prev node
                new_pair_tuple = (node1.prev.value + new_node.value, node1.prev.position, (node1.prev.node_id, new_node.node_id))
                # print('  adding new formed pair on heap: %r' % (new_pair_tuple,))
                heapq.heappush(pairs_heap, new_pair_tuple)

            if node2.next:
                if new_node.position == -1:
                    new_node.position = node2.next.position - 1

                invalidated_pairs.add((node2.node_id, node2.next.node_id))

                # new pair with the next one
                new_pair_tuple = (node2.next.value + new_node.value, new_node.position, (new_node.node_id, node2.next.node_id))
                # print('  adding new formed pair on heap (2): %r' % (new_pair_tuple,))
                heapq.heappush(pairs_heap, new_pair_tuple)

            merge_nodes(node1, node2, new_node)
            op_count += 1

        return op_count


if __name__ == '__main__':
    x = Solution()
    # print(x.minimumPairRemoval([5, 2, 3, 1]), 2)
    # print(x.minimumPairRemoval([2, 2, -1, 3, -2, 2]), 4)
    # print(x.minimumPairRemoval([2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]), 9)

    # print(x.minimumPairRemoval([2, 2, -1, 3, -2, 2, 1, 1, 1, -1]), 8)
    # print(x.minimumPairRemoval([2, 2, -1, 3, 0, 1, 1, 1, -1]), 7)
    # print(x.minimumPairRemoval([2, 2, -1, 3, 0, 1, 1, 0]), 6)
    # print(x.minimumPairRemoval([2, 1, 3, 0, 1, 1, 0]), 5)
    # print(x.minimumPairRemoval([2, 1, 3, 1, 1, 0]), 4)
    # print(x.minimumPairRemoval([2, 1, 3, 1, 1]), 3)
    # print(x.minimumPairRemoval([2, 1, 3, 2]), 2)
    # print(x.minimumPairRemoval([3, 3, 2]), 1)
    # print(x.minimumPairRemoval([3, 5]), 0)

    # print(x.minimumPairRemoval([3, 5]), 9)

    # print(x.minimumPairRemoval([2, 1, 3, 2]), 5)

    # FIXME: most likely WA due to issues calculating/maintaining "position"
    #  post merge
    print(x.minimumPairRemoval([0,-1,-4,2,4,-3,-1,3,4,-4,-4,4]), 9)