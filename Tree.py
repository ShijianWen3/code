from collections import deque


#二叉树节点实现
class Treenode:
    def __init__(self,value) -> None:
        self.value=value
        self.left:Treenode=None
        self.right:Treenode=None
        self.height:int=0

#二叉树数组实现
class ArrayTree:
    def __init__(self,array:list) -> None:
        self.array=array
        self.root_index=0
        

    def left(index:int):
        return index*2+1
    def right(index:int):
        return index*2+2
    def parent(index:int):
        return (index-1)//2
    
    def value(self,index:int):
        return self.array[index]
    #广度优先搜索，BFS
    def bfs(self)->list:
        result=list()
        for _ in range(self.root_index,len(self.array)):
            result.append(self.array[_])
        return result
    #深度优先搜索，DFS
    def dfs(self,index:int=0,result:list=None):
        if result is None:
            result=list()
        if index>=len(self.array):
            return None
        #前序遍历
        result.append(self.array[index])
        self.dfs(index*2+1,result)
        self.dfs(index*2+2,result)
        return result
    

#二叉搜索树实现
class BinarySearchTree:
    def __init__(self) -> None:
        self.rootnode:Treenode=None
    def insert(self,value):
        if self.rootnode is None:
            self.rootnode=Treenode(value)
        else:
            current,previous=self.rootnode,None
            while current is not None:
                previous=current
                if current.value<value:
                    current=current.right
                elif current.value>value:
                    current=current.left
                else:
                    return
            if previous.value<value:
                previous.right=Treenode(value)
            else:
                previous.left=Treenode(value)

    def search(self,value):
        if self.rootnode is None:
            return None
        current=self.rootnode
        while current is not None:
            if current.value<value:
                current=current.right
            elif current.value>value:
                current=current.left
            else:
                break
        return current
    
    def remove(self,value):
        if self.rootnode is None:
            return
        current,previous=self.rootnode,None
        while current is not None:
            if current.value<value:
                current=current.right
            elif current.value>value:
                current=current.left
            else:
                break
            previous=current
        else:
            raise IndexError('不存在该节点')
        #节点degree(度)等于0
        if (current.left is None) and (current.right is None):
            if previous.left==current:
                previous.left=None
            elif previous.right==current:
                previous.right=None
        #节点degree(度)等于1
        elif (current.left is None) or (current.right is None):
            if previous.left==current:
                previous.left=current.right or current.left
            elif previous.right==current:
                previous.right=current.right or current.left
        #节点degree(度)等于2，使用右子树最小值或左子树最大值替代节点值，并删除对应节点(树中不能存在重复元素)
        else:
            #用右子树的最小值替换被删除节点的节点值
            node:Treenode=current.right
            while node.left is not None:
                node_previous=node
                node=node.left
            else:
                current.value=node.value
                node_previous.left=None


            #用左子树的最大值替换被删除节点的节点值
            # node:Treenode=current.left
            # while node.right is not None:
            #     node_previous=node
            #     node=node.right
            # else:
            #     current.value=node.value
            #     node_previous.right=None


class AVLTree(BinarySearchTree):
    def __init__(self) -> None:
        self.rootnode:Treenode=None

    def height(self,node:Treenode):
        if node is None:
            return -1
        return node.height
    
    #平衡因子，判断旋转方法如何进行的依据
    def balance_factor(self,node:Treenode):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)
    

    def height_update(self,node:Treenode):
        node.height=max(self.height(node.left),self.height(node.right))+1
    
    def rotate_right(self,node:Treenode):
        child=node.left
        grand_child=child.right
        child.right=node
        node.left=grand_child
        self.height_update(node)
        self.height_update(child)
        return child
    
    def rotate_left(self,node:Treenode):
        child=node.right
        grand_child=child.left
        child.left=node
        node.right=grand_child
        self.height_update(node)
        self.height_update(child)
        return child
    
    def rotate(self,node:Treenode):
        balance_factor=self.balance_factor(node)
        #左偏树
        if balance_factor>1:
            if self.balance_factor(node.left)>=0:
                return self.rotate_right(node)
            else:
                node.left=self.rotate_left(node.left)
                return self.rotate_right(node)
        #右偏树
        elif balance_factor<-1:
            if self.balance_factor(node.right)<=0:
                return self.rotate_left(node)
            else:
                node.right=self.rotate_right(node.right)
                return self.rotate_left(node)
        else:
            return node
    def insert_helper(self,node:Treenode,value):
        if node is None:
            return Treenode(value)
        if value>node.value:
            node.right=self.insert_helper(node.right,value)
        elif value<node.value:
            node.left=self.insert_helper(node.left,value) 
        else:
            return node
        self.height_update(node)
        return self.rotate(node)
    
    def remove_helper(self,node:Treenode,value):
        if node is None:
            return None
        if value>node.value:
            node.right=self.remove_helper(node.right,value)
        elif value<node.value:
            node.left=self.remove_helper(node.left,value)
        else:
            if (node.left is None) or (node.right is None):
                child=node.left or node.right
                if child is None:
                    return None
                else:
                    node=child
            else:
                tmp=node.right
                while tmp.left is not None:
                    tmp=tmp.left
                node.value=tmp.value
                node.right=self.remove_helper(node.right,tmp.value)
        self.height_update(node)
        return self.rotate(node)


    def insert(self, value):
        self.rootnode=self.insert_helper(self.rootnode,value)
    def remove(self,value):
        self.rootnode=self.remove_helper(self.rootnode,value)
    def append(self,value):
        super().insert(value)    
                
    
    


    

    
#列表反序列化为二叉树
def list_to_tree(goal:list,index:int)->Treenode:
    if (index<0) or (index>=len(goal)) or (goal[index] is None):
        return None
    rootnode=Treenode(goal[index])
    rootnode.left=list_to_tree(goal,index*2+1)
    rootnode.right=list_to_tree(goal,index*2+2)
    return rootnode

#BFS，广度优先搜索
def bfs(goal:Treenode):
    queue=deque()
    queue.append(goal)
    result=list()
    while queue:
        node=queue.popleft()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result
#DFS，深度优先搜索
def dfs(goal:Treenode,result:list=None):
    #只在第一层创建列表储存结果
    if result is None:
        result=list()
    if goal is None:
        return None
    #前序遍历
    # result.append(goal.value)
    dfs(goal.left,result)
    #中序遍历
    result.append(goal.value)
    dfs(goal.right,result)
    #后序遍历
    # result.append(goal.value)
    return result

    



# # "Driver Code"
# if __name__ == '__main__':
#     tmp=[1,2,6,5,7,3,5]
#     # mytree=ArrayTree(tmp)
#     # print(mytree.dfs())
#     # print(mytree.bfs())
#     bst=BinarySearchTree()
#     for _ in range(len(tmp)):
#         bst.insert(tmp[_])
#     print(bst.search(3))
#     print(bst.search(8))
#     print(bfs(bst.rootnode))
#     print(dfs(bst.rootnode))

if __name__=='__main__':
    tmp=[7,6,8,5,9,4,10,3,11,2,12,1,13]
    avltree=AVLTree()
    for _ in range(len(tmp)):
        # avltree.append(tmp[_])
        #待解决，按二叉搜索树insert方法插入和重写的每次插入会旋转保证平衡的insert方法，二者结果按bfs遍历出来结果不一样
        avltree.insert(tmp[_])
    print(dfs(avltree.rootnode))
    print(bfs(avltree.rootnode))



    