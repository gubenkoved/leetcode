from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '<Node %s>' % self.val


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        cur = head
        size = 0

        while cur is not None:
            size += 1
            cur = cur.next

        # now sort using merge sort technique using bucket sizes that grows
        # exponentially
        bucket_size = 1

        def step(ptr, n):
            k = n
            result = ptr
            while k > 0 and result is not None:
                result = result.next
                k -= 1
            return result

        # rolling new head from round to round
        new_head = head

        while bucket_size < size:
            bucket_start = new_head
            prev_bucket_end = None

            # print('sorting with bucket size of %d' % bucket_size)

            is_first_bucket_of_this_size = True

            while bucket_start:
                # print(' handling bucket')
                next_bucket_start = step(bucket_start, bucket_size * 2)

                new_bucket_head = None
                new_bucket_cur = None

                a = bucket_start
                b = step(bucket_start, bucket_size)

                a_steps = 0
                b_steps = 0

                while a_steps + b_steps < 2 * bucket_size:
                    if a is None:
                        break

                    if b is None or b_steps >= bucket_size or a_steps < bucket_size and a.val < b.val:
                        picked = a
                        a = a.next
                        a_steps += 1
                    else:  # step with b pointer
                        picked = b
                        b = b.next
                        b_steps += 1

                    # wire in picked to the bucket
                    if new_bucket_head is None:
                        new_bucket_head = picked
                        new_bucket_cur = picked
                    else:
                        new_bucket_cur.next = picked
                        new_bucket_cur = picked

                    # unless wired in explicitly we replace next pointer on already
                    # sorted items in bucket with null
                    new_bucket_cur.next = None

                    if is_first_bucket_of_this_size:
                        is_first_bucket_of_this_size = False
                        new_head = new_bucket_head

                    # final bucket edge case
                    if b is None and a_steps == bucket_size:
                        break

                if prev_bucket_end is not None:
                    prev_bucket_end.next = new_bucket_head
                prev_bucket_end = new_bucket_cur

                # move bucket start pointer
                bucket_start = next_bucket_start

            # print_list(new_head)

            bucket_size *= 2

        return new_head


def create_list(arr):
    head = ListNode(arr[0])
    cur = head

    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next

    return head


def print_list(head):
    cur = head

    while cur is not None:
        print('%s -> ' % cur.val, end='')
        cur = cur.next

    print('nil')


if __name__ == '__main__':


    x = Solution()
    print_list(x.sortList(create_list([5, 4, 1, 2, 9, 0, 5])))
    # print_list(x.sortList(create_list([1, 2])))
    # print_list(x.sortList(create_list([2, 1])))
    # print_list(x.sortList(create_list([3, 2, 1])))
    # print_list(x.sortList(create_list([4, 3, 2, 1])))
    # print_list(x.sortList(create_list([5, 4, 3, 2, 1])))
