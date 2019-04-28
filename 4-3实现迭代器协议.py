"""
实现迭代器协议
"""

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []


    def __repr__(self):
        return 'Node({!r})'.format(self._value)


    def add_child(self,node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)


    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():   # 返回root 然后再调用__iter__
        print(ch)


# 方案二  代理难懂，不建议使用
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []


    def __repr__(self):
        return 'Node({!r})'.format(self._value)


    def add_child(self,node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)


    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class DepthFirstIterator:
    def __init__(self,start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = Node


    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node


        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)

                return nextchild
            except StopIteration:
                self._child_iter = Node
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)