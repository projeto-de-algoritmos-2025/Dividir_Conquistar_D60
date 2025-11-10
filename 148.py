from typing import Optional, List

class Solution:
    def sortList(self, head: Optional['ListNode']) -> Optional['ListNode']:

        if not head or not head.next:
            return head

        def length(node: Optional['ListNode']) -> int:
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        def select_kth_value(node: Optional['ListNode'], k: int, n: int) -> int:

            vals: List[int] = []
            cur = node
            while cur:
                vals.append(cur.val)
                cur = cur.next

            def median_of_medians(arr: List[int], kk: int) -> int:

                if len(arr) <= 5:
                    arr.sort()
                    return arr[kk]

                groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
                meds: List[int] = []
                for g in groups:
                    g.sort()
                    meds.append(g[len(g) // 2])
                pivot = median_of_medians(meds, len(meds) // 2)

                lt: List[int] = []
                eq: List[int] = []
                gt: List[int] = []
                for v in arr:
                    if v < pivot:
                        lt.append(v)
                    elif v > pivot:
                        gt.append(v)
                    else:
                        eq.append(v)

                if kk < len(lt):
                    return median_of_medians(lt, kk)
                elif kk < len(lt) + len(eq):
                    return pivot
                else:
                    return median_of_medians(gt, kk - len(lt) - len(eq))

            return median_of_medians(vals, k)

        def partition(node: Optional['ListNode'], pivot: int):
            less_head = less_tail = None
            eq_head = eq_tail = None
            greater_head = greater_tail = None

            cur = node
            while cur:
                next_node = cur.next
                cur.next = None
                if cur.val < pivot:
                    if not less_head:
                        less_head = less_tail = cur
                    else:
                        less_tail.next = cur
                        less_tail = cur
                elif cur.val > pivot:
                    if not greater_head:
                        greater_head = greater_tail = cur
                    else:
                        greater_tail.next = cur
                        greater_tail = cur
                else:
                    if not eq_head:
                        eq_head = eq_tail = cur
                    else:
                        eq_tail.next = cur
                        eq_tail = cur
                cur = next_node

            return (less_head, less_tail, eq_head, eq_tail, greater_head, greater_tail)

        def concat(a_head, a_tail, b_head, b_tail):
            if not a_head:
                return b_head, b_tail
            if not b_head:
                return a_head, a_tail
            a_tail.next = b_head
            return a_head, b_tail

        def quicksort(node: Optional['ListNode'], n: int):
            if not node or not node.next:
                return node, node

            pivot = select_kth_value(node, n // 2, n)
            l_h, l_t, e_h, e_t, g_h, g_t = partition(node, pivot)

            def size(x: Optional['ListNode']) -> int:
                sz = 0
                c = x
                while c:
                    sz += 1
                    c = c.next
                return sz

            left_head, left_tail = quicksort(l_h, size(l_h)) if l_h else (None, None)
            right_head, right_tail = quicksort(g_h, size(g_h)) if g_h else (None, None)

            head1, tail1 = (concat(left_head, left_tail, e_h, e_t)
                            if e_h else (left_head, left_tail))
            head2, tail2 = concat(head1, tail1, right_head, right_tail)
            return head2, tail2

        n = length(head)
        sorted_head, _ = quicksort(head, n)
        return sorted_head