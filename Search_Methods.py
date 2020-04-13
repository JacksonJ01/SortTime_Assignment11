# Jackson J.
# 4.10.2020
# This file contains 5 search methods, 2 of which are recursive, while the other 3 are iterative.


# This is the Bubble_Sort method. It sorts by checking 2 values at a time.
# Starting at the front of the list, it compares the first value to to the second value, and puts them in ascending order.
# From there it compares the second and third value, and so on. All of this is done with loops.
def Bubble_Sort(lists):
    amount = len(lists)
    for a in range(amount - 1):
        swapped = False
        for b in range(0, amount - 1 - a):
            if lists[b] > lists[b+1]:
                lists[b], lists[b+1] = lists[b+1], lists[b]
                swapped = True
        if swapped is False:
            break
    return lists


# This is the Insertion_Sort method.
# It sorts by arranging the data into it's correct position by sorting it into the left side of the list as it reaches it.
# If zero is the smallest value, and is at the end of the list,
# it will move the zero all the way to the beginning of the list. All of this is done with loops#
def Insertion_Sort(lists):
    amount = len(lists)
    for a in range(1, amount):
        for b in range(a - 1, -1, -1):  # Sidenote: I went on YouTube for more help and to understand on these sorts, and he had (a-1, 0, -1).
                                        # This did not work for me and it kept putting 5 at the beginning. I didn't think -1 would work
            if lists[b] > lists[b + 1]:
                lists[b], lists[b + 1] = lists[b + 1], lists[b]
            else:
                break
    return lists


# This is the Selection_Sort method. It sorts by finding the smallest value in a list, then moving it to the front of the list
# All of this is done with loops
def Selection_Sort(lists):
    amount = len(lists)
    for a in range(0, amount - 1):
        smallest = a
        for b in range(a + 1, amount):
            if lists[b] < lists[smallest]:
                smallest = b
        lists[a], lists[smallest] = lists[smallest], lists[a]
    return lists


# This is the Merge_Sort method. It sorts by dividing the list in 2, then dividing those in two, and so on.
# This sorts the loop while it splits it
# All of this is done through recursion with a smidge of iterative
def Merge_Sort(lists):
    if len(lists) <= 1:
        return lists
    mid = int(len(lists) / 2)
    left, right = Merge_Sort(lists[:mid]), Merge_Sort(lists[mid:])
    return merge(left, right)


def merge(left, right):
    results = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            results.append(left[left_pointer])
            left_pointer += 1
        else:
            results.append(right[right_pointer])
            right_pointer += 1
    results.extend(left[left_pointer:])
    results.extend(right[right_pointer:])
    return results


# This is the Quick_Sort method. It sorts by taking a value, whether it be the first, middle, or last value, and uses the value to compare the other items in the list.
# Each time it sorts it into higher or lower lists which are then sorted through recursion.
def Quick_Sort(lists):
    amount = len(lists)
    if amount <= 1:
        return lists
    else:
        # One guy on YouTube had this method where you search 3 values for your pivot, but his code wasn't working for me(surprise)
        # Another guy used the last value as the pivot, but I read above how that could be inefficient.
        # So I combined the second guy's code and the other guy's idea
        front = lists[0]
        end = lists[-1]
        half = lists[int(amount / 2)]
        if half > front > end or half < front < end:
            pivot = front
            lists.remove(front)
        elif front < end < half or front > end > half:
            pivot = end
            lists.remove(end)
        else:
            pivot = half
            lists.remove(half)
    greater = []
    lower = []

    for value in lists:
        if value > pivot:
            greater.append(value)
        else:
            lower.append(value)
    return Quick_Sort(lower) + [pivot] + Quick_Sort(greater)
