class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return f'[{self.left} | {self.val} | {self.right}]'


def binary_insert(root, node):
    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            binary_insert(root.left, node)
    elif node.val > root.val:
        if root.right is None:
            root.right = node
        else:
            binary_insert(root.right, node)

def find(root, val):
    if val < root.val:
        if root.left is None:
            return None
        return find(root.left, val)
    elif val > root.val:
        if root.right is None:
            return None
        return find(root.right, val)
    else:
        return root

def print_preorder(root):
    #https://en.wikipedia.org/wiki/Tree_traversal#Implementations
    if root is None:
        return
    print(root.val)
    print_preorder(root.left)
    print_preorder(root.right)

def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.val)
    print_inorder(root.right)

def print_postorder(root):
    if root is None:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val)

def print_levelorder(root):
    #http://stackoverflow.com/a/1894914
    thislevel = [root]
    while thislevel:
        nextlevel = []
        for node in thislevel:
            print(node.val, end=' ')
            if node.left is not None:
                nextlevel.append(node.left)
            if node.right is not None:
                nextlevel.append(node.right)
        print()
        thislevel = nextlevel


def main():
    root = Node(50)
    print(root)
    lst = [100, 200, 150, 25, 2, 37, 36, 38]
    for val in lst:
        binary_insert(root, Node(val))
        print("\nTree after inserting "+str(val)+":")
        print(root)

    print('--')

    print(find(root, 25))
    print(find(root, 42))

    print('--')

    print("in-order:")
    print_inorder(root)

    print("pre-order:")
    print_preorder(root)

    print("post-order:")
    print_postorder(root)

    print("level-order:")
    print_levelorder(root)


if __name__ == "__main__":
    main()
