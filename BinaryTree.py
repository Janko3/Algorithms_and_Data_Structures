import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


class BinaryTreeNode():
    def __init__(self, value, parent=None, left=None, right=None):
        self._value = value
        self._parent = parent
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._value)


def inorder(node):
    if not node._left is None:
        print("(", end="")
        inorder(node._left)
    print(node._value, end="")
    if not node._right is None:
        inorder(node._right)
        print(")", end="")


def eval_expression(node):
    if node._left is None and node._right is None:
        return int(node._value)
    else:
        x = eval_expression(node._left)
        y = eval_expression(node._right)
        op = node._value
        result = ops[op](x, y)
        return result


x = BinaryTreeNode('+')
y = BinaryTreeNode('*')
z = BinaryTreeNode('*')

x._left = y
y._parent = x
x._right = z
z._parent = x

a = BinaryTreeNode('2')
b = BinaryTreeNode('-')

y._left = a
a._parent = y
y._right = b
b._parent = y

c = BinaryTreeNode('3')
d = BinaryTreeNode('1')

z._left = c
c._parent = z
z._right = d
d._parent = z

e = BinaryTreeNode('2')
f = BinaryTreeNode('1')

b._left = e
e._parent = b
b._right = f
f._parent = b


inorder(x)
print("=", end="")
print(eval_expression(x))
