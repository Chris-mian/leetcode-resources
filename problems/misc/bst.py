

class Node:
    def __init__(self, key, value):
        self.left: "Node" | None = None
        self.right: "Node" | None = None
        self.key = key
        self.value = value

    def insert(self, key, value):
        if self.key == key:
            raise ValueError("Duplicated key is prohibited")
        elif self.key > key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        else: # self.key < key
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.insert(key, value)

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key > key:
            if self.left is None:
                return None
            else:
                return self.left.get(key)
        else: # self.key < key
            if self.right is None:
                return None
            else:
                return self.right.get(key)

    def delete(self, key, root_node):
        if self.key == key:
            if self.left is None and self.right is None:
                new_node = None
            elif self.left is None:
                new_node = self.right
            elif self.right is None:
                new_node = self.left
            else: # Both left and right subtrees exists
                new_k, new_v = self.right.find_min()
                new_node = Node(new_k, new_v)
                new_node.left = self.left
                self.right.delete(new_k, self)
                new_node.right = self.right
            if root_node is not None:
                if root_node.key > new_node.key:
                    root_node.left = new_node
                elif root_node.key < new_node.key:
                    root_node.right = new_node
                else:
                    raise ValueError("Impossible case")
            return self.value
                
        elif self.key > key:
            if self.left is None:
                return None
            else:
                return self.left.delete(key, self)
        else: # self.key < key
            if self.right is None:
                return None
            else:
                return self.right.delete(key, self)
            
    def find_min(self):
        if self.left is None:
            return (self.key, self.value)
        else:
            return self.left.find_min()

class BST:
    def __init__(self):
        self.root: Node | None = None

    # check current subtree at the root,
    # when it's larger than root => insert in right subtree.
    # when it's smaller than root => insert in left subtree
    # under the condition that 
    def insert(self, key, val):
        # self._insert_recursive(Node(key, val), self.root)
        if self.root is None:
            self.root = Node(key,val)
        else:
            self.root.insert(key, val)
            
        
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)
    
    
    def delete(self, key):
        if self.root is None:
            return None
        else:
            return self.root.delete(key)