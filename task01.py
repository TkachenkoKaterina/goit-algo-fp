class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 1. Реверсування однозв'язного списку
def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


# 2. Сортування злиттям для однозв'язного списку
def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


# 3. Об'єднання двох відсортованих списків
def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)

    print("Оригінальний список:")
    ll.print_list()

    reverse_list(ll)
    print("Реверсований список:")
    ll.print_list()

    ll.head = merge_sort(ll.head)
    print("Відсортований список:")
    ll.print_list()

    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    merged_head = merge_two_sorted_lists(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
