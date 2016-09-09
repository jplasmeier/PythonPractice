# Practice with implementing algorithms on Trees and Graphs
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

import copy
import Queue

def flatten_list(to_flat):
    flat = []
    if to_flat is None:
        return []
    for i in to_flat:
        if isinstance(i, int):
            flat.append(i)
        elif isinstance(i, list):
            flat.extend(flatten_list(i))
    return flat


class TreeNode:

    def __init__(self, value, left, right):
        self.value = value
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        self.checked = False

    def print_tree_preorder(self):
        print str(self.value)
        if hasattr(self, 'left'):
            self.left.print_tree_preorder()
        if hasattr(self, 'right'):
            self.right.print_tree_preorder()
    
    def flatten_tree_preorder(self):
        lst = [self.value]
        if hasattr(self, 'left'):
            lst.append(self.left.flatten_tree_preorder())
        if hasattr(self, 'right'):
            lst.append(self.right.flatten_tree_preorder())
        return lst

    def flatten_tree_inorder(self):
        lst = []
        if hasattr(self, 'left'):
            lst.append(self.left.flatten_tree_inorder())
        lst.append(self.value)
        if hasattr(self, 'right'):
            lst.append(self.right.flatten_tree_inorder())
        return lst

    def flatten_tree_postorder(self):
        lst = []
        if hasattr(self, 'left'):
            lst.append(self.left.flatten_tree_postorder())
        if hasattr(self, 'right'):
            lst.append(self.right.flatten_tree_postorder())
        lst.append(self.value)
        return lst

    def flatten_tree_levelorder(self):
        lst = [self.value]
        q = []
        if hasattr(self, 'left') and not self.left.checked:
            self.left.checked = True
            q.append(self.left)
        if hasattr(self, 'right') and not self.right.checked:
            self.right.checked = True
            q.append(self.right)
        while q:
            node = q.pop(0)
            lst.append(node.value)
            if hasattr(node, 'left') and not node.left.checked:
                node.left.checked = True
                q.append(node.left)
            if hasattr(node, 'right') and not node.right.checked:
                node.right.checked = True
                q.append(node.right)
        return lst

    #TODO: Reimplement for graphs - doesn't give us much for trees
    def is_path_to(self, target):
        if self.value == target.value:
            print 'fouund itt'
            return True
        if hasattr(self, 'left'):
            self.left.is_path_to(target)
        if hasattr(self, 'right'):
            self.right.is_path_to(target)
        return False

class GraphNode:

    adjacent = []

    def __init__(self, value, adjacent):
        self.value = value
        self.marked = False
        self.adjacent = adjacent

    def print_graph_depth_first(self):
        print self.value
        self.marked = True
        if hasattr(self,'adjacent'):
            for neighbor in self.adjacent:
                try:
                    if neighbor.marked is False:
                        neighbor.print_graph_depth_first()
                except:
                    pass

    def print_graph_breadth_first(self):
        print self.value
        items = []
        self.marked = True
        items.append(self) 

        while items is not None:
            print item.value
             

    def graph_to_list_closure(self,lst=[]):
        def graph_to_list_depth_first(node):
            lst.append(node.value)
            node.marked = True
            if hasattr(node,'adjacent'):
                for neighbor in node.adjacent:
                    try:
                        if neighbor.marked is False:
                            graph_to_list_depth_first(neighbor)
                    except:
                        pass
        graph_to_list_depth_first(self)
        return lst

#Build you a tree
#       5
#      / \
#     3   4
#      \
#       2
#      / \
#     0   1
t0 = TreeNode(0,None, None)
t1 = TreeNode(1,None, None)
t2 = TreeNode(2, t0, t1)
t3 = TreeNode(3, None, t2)
t4 = TreeNode(4, None, None)
t5 = TreeNode(5, t3, t4)
assert [5,3,2,0,1,4] == flatten_list(t5.flatten_tree_preorder())
assert [3,0,2,1,5,4] == flatten_list(t5.flatten_tree_inorder())
assert [0,1,2,3,4,5] == flatten_list(t5.flatten_tree_postorder())
assert [5, 3, 4, 2, 0, 1] == flatten_list(t5.flatten_tree_levelorder())

def tree_to_list_of_lists(root):
    list_of_lists = []
    current = []
    if (root is not None):
        current.append(root)
    while len(current) > 0:
        list_of_lists.append(current)
        parents = copy.deepcopy(current)
        current = []
        for node in parents:
            if hasattr(node, 'left'):
                current.append(node.left)
            if hasattr(node, 'right'):
                current.append(node.right)
    return list_of_lists

lol = tree_to_list_of_lists(t5)
for l in lol:
    print '['
    for t in l:
        print '[', t.value, ']'
    print ']'

#Build you a graph
g0 = GraphNode(0, [])
g1 = GraphNode(1, [])
g2 = GraphNode(2, [g0, g1])
g3 = GraphNode(3, [g2])
g4 = GraphNode(4, [g0])
g5 = GraphNode(5, [g3, g4])
g1.left = g5
#print g5.print_graph_depth_first()
#print g5.print_graph_breadth_first()
#print g5.graph_to_list_closure([])
