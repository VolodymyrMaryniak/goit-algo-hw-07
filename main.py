from avl_tree import AVLNode, insert


def get_max_value(root: AVLNode):
    if root.right:
        return get_max_value(root.right)

    return root.key


def get_min_value(root: AVLNode):
    if root.left:
        return get_min_value(root.left)

    return root.key


def get_sum(root: AVLNode):
    if not root:
        return 0

    return root.key + get_sum(root.left) + get_sum(root.right)


def main():
    root: AVLNode = None

    for i in range(1, 13):
        root = insert(root, i)

    print("AVL Tree:")
    print(root)

    # Task 1
    print("\n\nTask 1")
    print("Max value: ", get_max_value(root))

    # Task 2
    print("\n\nTask 2")
    print("Min value: ", get_min_value(root))

    # Task 3
    print("\n\nTask 3")
    print("Sum of all nodes values: ", get_sum(root))


if __name__ == "__main__":
    main()
