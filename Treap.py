class Treap:
    def __init__(self, x, y, left=None, right=None):
        self.x = x
        self.y = y
        self.left = left
        self.right = right

    def merge(self, left, right):
        if left is None:
            return right

        if right is None:
            return left

        if left.y > right.y:
            new_right = self.merge(left.right, right)
            return Treap(left.x, left.y, left.left, new_right)
        else:
            new_left = self.merge(right.left, left)
            return Treap(right.x, right.y, new_left, right.right)

    def split(self, x, left, right):
        new_tree = None

        if self.x <= x:

            if self.right is None:
                right = None
            else:
                self.right.split(x, new_tree, right)

            left = Treap(x, self.y, self.left, new_tree)

        else:

            if self.left is None:
                left = None
            else:
                self.left.split(x, left, new_tree)

            right = Treap(x, self.y, new_tree, self.right)
