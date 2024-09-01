from collections import deque


class AdjMatrixGrapg:
    def __init__(self,vertex:list,edges:list[list]) -> None:
        self.vertex:list=[]
        self.adjmatrix:list[list]=[]
        for _ in vertex:
            self.vertex_append(_)
        for _ in edges:
            self.edge_add(_[0],_[1])
    def vertex_append(self,value):
        self.vertex.append(value)
        new_row=[0]*(len(self.vertex)-1)
        self.adjmatrix.append(new_row)
        for _ in self.adjmatrix:
            _.append(0)
    
    def edge_add(self,index1:int,index2:int):
        if index1<0 or index2<0 or index1>=len(self.vertex) or index2>=len(self.vertex):
            raise IndexError('访问越界')
        self.adjmatrix[index1][index2]=1
        self.adjmatrix[index2][index1]=1

    def vertex_remove(self,index:int):
        if index<0 or index>=len(self.adjmatrix):
            raise IndexError('访问越界')
        self.vertex.pop(index)
        self.adjmatrix.pop(index)
        for _ in self.adjmatrix:
            _.pop(index)
    
    def edge_remove(self,index1:int,index2:int):
        if index1<0 or index2<0 or index1>=len(self.vertex) or index2>=len(self.vertex):
            raise IndexError('访问越界')
        self.adjmatrix[index1][index2]=0
        self.adjmatrix[index2][index1]=0
    
    def printf(self):
        print('#',end=' ')
        for _ in self.vertex:
            print(_,end=' ')
        else:
            print()
        i=0
        for _ in self.adjmatrix:
            print(self.vertex[i],end=' ')
            for item in _:
                print(item,end=' ')
            else:
                print()
                i+=1

class Vertex:
    def __init__(self,value) -> None:
        self.value=value
class AdjTableGraph:
    def __init__(self,edges:list[list[Vertex]]) -> None:
         self.adjtable=dict[Vertex:list[Vertex]]()
         for _ in edges:
             self.vertex_append(_[0])
             self.vertex_append(_[1])
             self.edge_add(_[0],_[1])

    def vertex_append(self,vertex:Vertex):
        if vertex in self.adjtable:
            return
        self.adjtable[vertex]=list[Vertex]()

    def edge_add(self,vertex1:Vertex,vertex2:Vertex):
        if vertex1 not in self.adjtable or vertex2 not in self.adjtable or vertex1==vertex2:
            raise ValueError
        if vertex1 in self.adjtable[vertex2] or vertex2 in self.adjtable[vertex1]:
            return
        self.adjtable[vertex1].append(vertex2)
        self.adjtable[vertex2].append(vertex1)

    def vertex_remove(self,vertex:Vertex):
        if vertex not in self.adjtable:
            raise ValueError('不存在该节点')
        self.adjtable.pop(vertex)
        for _ in self.adjtable.values:
            if vertex in _:
                _.remove(vertex)

    def edge_remove(self,vertex1:Vertex,vertex2:Vertex):
        if vertex1 not in self.adjtable or vertex2 not in self.adjtable or vertex1==vertex2:
            raise ValueError
        self.adjtable[vertex1].remove(vertex2)
        self.adjtable[vertex2].remove(vertex1)

    def vertex(self,value):
        for _ in self.adjtable.keys():
            if _.value==value:
                return _
        else:
            raise ValueError('不存在该顶点')

    def printf(self):
        for vertex,edges in self.adjtable.items():
            print(vertex.value,end=':')
            for _ in edges:
                print(_.value,end=' ')
            print()
    

def list_to_vertex(goal:list[list]):
    result=list[list[Vertex]]()
    for _ in goal:
        result.append([Vertex(_[0]),Vertex(_[1])])
    return result

#图的广度优先搜索bfs，未考虑非连通图
def bfs(graph:AdjTableGraph,start:Vertex)->list:
    result=list()
    bfs_deque=deque([start])
    # bfs_deque.append(start)
    visited=set([start])
    while len(bfs_deque)>0:
        vertex=bfs_deque.popleft()
        result.append(vertex.value)
        for _ in graph.adjtable[vertex]:
            if _ in visited:
                continue
            bfs_deque.append(_)
            visited.add(_)
        # for _ in graph.adjtable[vertex]:
        #     if _  not in visited:
        #         bfs_deque.append(_)
        #         visited.add(_)
    else:
        return result


#图的深度优先搜索dfs，未考虑连通图        
def dfs(graph:AdjTableGraph,start:Vertex,result:list,visited:set=None)->list:
    if visited is None:
        visited=set()
    result.append(start.value)
    visited.add(start)
    for _ in graph.adjtable[start]:
        if _ in visited:
            continue
        dfs(graph,_,result,visited)



if __name__=='__main__':
    # vertex=[1,2,6,5,7,3]
    edges=[[0,2],[3,4],[1,5]]
    
    # graph=AdjMatrixGrapg(vertex,edges)
    
    graph=AdjTableGraph(list_to_vertex(edges))

    print(bfs(graph,graph.vertex(0)))
    result=[]
    dfs(graph,graph.vertex(0),result)
    print(result)







