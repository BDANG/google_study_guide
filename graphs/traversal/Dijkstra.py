import sys
import heapq

def simplify_parent_list(parent, start, end):
    new = []
    current = end

    while current != -1:
        new.append(current)
        current = parent[current]
    return list(reversed(new))



def path(graph, start, end=None):
    return path_and_value(graph, start, end)[0]

def value(graph, start, end=None):
    return path_and_value(graph, start, end)[1]

def path_and_value(graph, start, end=None):

    if end:
        heap = []

        parent = [None for i in range(graph.numVertices)]
        parent[start] = -1
        current = start

        currentWeight = 0
        visited = set()

        found = False

        while len(visited) != graph.numVertices:
            if current == end:
                found = True
                break

            if current not in visited:
                #print(current, currentWeight)
                visited.add(current)
                neighbors = graph.get_neighbors(current)

                for neighbor, weight in neighbors:
                    if neighbor not in visited:
                        if not parent[neighbor]:
                            parent[neighbor] = current
                        heapq.heappush(heap, (weight+currentWeight, neighbor))

            if heap:
                (currentWeight, current) = heapq.heappop(heap)
            else:
                break

        if found:
            parent = simplify_parent_list(parent, start, end)
            return parent, currentWeight
        else:
            return None, -1


    #else:
