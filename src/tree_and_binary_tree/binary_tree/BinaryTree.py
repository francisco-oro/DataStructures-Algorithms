# Binary Tree
# Time complexity: O(n)
# Space complexity: O(n)
import sys
sys.path.insert(1, 'C:/Users/ASUS/source/repos/dsa/src')
print(sys.path)

from queue_1 import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

tea = TreeNode("tea")
coffee = TreeNode("coffee")

leftChild.left_child = tea
leftChild.right_child = coffee

newBT.left_child=leftChild
newBT.right_child=rightChild

# PreOrder Traversal
# Time complexity: O(n)
# Space complexity: O(n)

def preOrderTraversal(rootNode:TreeNode):
    if not rootNode: # O(1)
        return 
    print(rootNode.data) # O(1)
    preOrderTraversal(rootNode.left_child) # O(n/2)
    preOrderTraversal(rootNode.right_child) # O(n/2)

# InOrder Traversal
# Time complexity: O(n)
# Space complexity: O(n)

def inOrderTraversal(rootNode:TreeNode):
    if not rootNode: # O(1)
        return 
    inOrderTraversal(rootNode.left_child) # O(n/2)
    print(rootNode.data) # O(1)
    inOrderTraversal(rootNode.right_child) # O(n/2)

# PostOrder Traversal
# Time complexity: O(n)
# Space complexity: O(n)

def postOrderTraversal(rootNode:TreeNode):
    if not rootNode: # O(1)
        return
    postOrderTraversal(rootNode.left_child) # O(n/2)
    postOrderTraversal(rootNode.right_child) # O(n/2)
    print(rootNode.data) # O(1)

# LevelOrder Traversal
# Time complexity: O(n)
# Space complexity: O(n)

def levelOrderTraversal(rootNode:TreeNode):
    if not rootNode: # O(1)
        return
    else: 
        customQueue = queue.Queue() # O(1)
        customQueue.enqueue(rootNode) # O(1)
        while not(customQueue.isEmpty()): # O(n) 
            root = customQueue.dequeue() # O(1)
            print(root.value.data)

            if (root.value.left_child is not None): # O(n)
                customQueue.enqueue(root.value.left_child)

            if (root.value.right_child is not None): # O(n)
                customQueue.enqueue(root.value.right_child)


# Search for a node using levelorder Traversal
# Time complexity: O(n)
# Space complexity: O(n)

def searchBT(rootNode:TreeNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "success"
            
            if (root.value.left_child is not None): # O(n)
                customQueue.enqueue(root.value.left_child)

            if (root.value.right_child is not None): # O(n)
                customQueue.enqueue(root.value.right_child)
        
        return "Not found"
    
# Search for a binary tree insertion 
# Time complexity: O(n)
# Space complexity: O(n)

def insertNodeBT(rootNode:TreeNode, newNode:TreeNode):
    if not rootNode:
        rootNode = newNode
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            if(root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            
            else:
                root.value.left_child = newNode
                return "Succesfully inserted"
            
            if(root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)
            
            else:
                root.value.right_child = newNode
                return "Succesfully inserted"
        
def getDeepestNode(rootNode:TreeNode):
    if not rootNode:
        return
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            if (root.value.left_child is not None): # O(n)
                customQueue.enqueue(root.value.left_child)

            if (root.value.right_child is not None): # O(n)
                customQueue.enqueue(root.value.right_child)

        deepestNode = root.value
        return deepestNode
    
def deleteDeepestNode(rootNode:TreeNode, dNode:TreeNode):
    if not rootNode:
        return
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            
            if root.value.right_child:
                if root.value.right_child is dNode:
                    root.value.right_child = None
                    return
                else: 
                    customQueue.enqueue(root.value.right_child)

            if root.value.left_child:
                if root.value.left_child is dNode:
                    root.value.left_child = None
                    return
                else: 
                    customQueue.enqueue(root.value.left_child)

# Node Deletion
# Time complexity: O(n)
# Space complexity: O(n)

def deleteNodeBT(rootNode:TreeNode, node:TreeNode):
    if not rootNode: # O(1)
        return "The BT does not exist"
    
    else: 
        customQueue = queue.Queue() # O(1)
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)

                return "The node has been succesfully deleted"

            if (root.value.left_child is not None): # O(n)
                customQueue.enqueue(root.value.left_child) # O(1)

            if (root.value.right_child is not None): # O(n)
                customQueue.enqueue(root.value.right_child)
        return "Failed to delete"
    
def deleteBT(rootNode:TreeNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None

    return "The BT has been succesfully deleted"

deleteBT(newBT)
levelOrderTraversal(newBT)