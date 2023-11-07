# Create a BST
# Time complexity: O(1)
# Space complexity: O(1)

class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None


def insertNode(rootNode:BSTNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left_child is None:
            rootNode.left_child = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left_child, nodeValue)
    else:
        if rootNode.right_child is None:
            rootNode.right_child = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right_child, nodeValue)

    return "The node has been succesfully inserted"

newBST = BSTNode(None) # O(1)
print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(newBST.data)
print(newBST.left_child.data)