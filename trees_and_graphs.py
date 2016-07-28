# Practice with implementing algorithms on Trees and Graphs
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

import Queue

class TreeNode:

    def __init__(self, value, left, right):
        self.value = value
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        self.checked = False

    def print_tree_preorder(self, offset=''):
        print offset+str(self.value)
        if hasattr(self, 'left'):
            print offset+"|"
            self.left.print_tree_preorder()
        if hasattr(self, 'right'):
            print offset+"    \\"
            self.right.print_tree_preorder("    "+offset)
    
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
        q = Queue.Queue()


    def graph_to_list_closure(self,lst=[]):
        #Closure likely isn't needed but is this a violation of any practice/standard? 
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
t0 = TreeNode(0,None, None)
t1 = TreeNode(1,None, None)
t2 = TreeNode(2, t0, t1)
t3 = TreeNode(3, None, t2)
t4 = TreeNode(4, None, None)
t5 = TreeNode(5, t3, t4)
#t5.print_tree_preorder()

#Build you a graph
g0 = GraphNode(0, [])
g1 = GraphNode(1, [])
g2 = GraphNode(2, [g0, g1])
g3 = GraphNode(3, [g2])
g4 = GraphNode(4, [g0])
g5 = GraphNode(5, [g3, g4])
g1.left = g5
print g5.print_graph_depth_first()
#print g5.graph_to_list_closure([])
