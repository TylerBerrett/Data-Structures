import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # base = self.value
        new_tree = BinarySearchTree(value)

        if new_tree.value >= self.value:
            if self.right is None:
                self.right = new_tree
            else:
                self.right.insert(value)

        else:
            if self.left is None:
                self.left = new_tree
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right:
                if self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)
            else:
                return False

        elif target == self.value:
            return True

        else:
            if self.left:
                if self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        right = self.right
        if right:
            while right.right:
                right = right.right
            return right.value
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.value:
            cb(self.value)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        if self.value:
             print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node:
            queue = Queue()
            queue.enqueue(node)
        while queue.len():
            current = queue.dequeue()
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node:
            stack = Stack()
            stack.push(node)
        while stack.len():
            current = stack.pop()
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


test = BinarySearchTree(8)
test.insert(3)
test.insert(10)
test.insert(1)
test.insert(6)
test.insert(4)
test.insert(7)
test.insert(14)
test.insert(13)