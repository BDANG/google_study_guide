(**Example code requires Python3**)
# High Level Review


### Algorithms
### Sorting
* `Mergesort`
    * Divide and conquer, recursively divide until 1-element array
    * Recursively build up the splits in sorted order. Pick the smaller element between two subarrays
    * `Runtime`: O(nlogn) worst case
    * `Space`: O(n) auxiliary
    * Stable sort
* `Quicksort`
    * Select a pivot and sort elements to the right or left of the pivot
    * `Runtime`: O(n^2) worst case, O(nlogn) average
    * `Space`: O(1) in place or O(n) auxiliary
    * NOT STABLE
### Hashtables
* `Overview`
    * A symbol table (key-value) for O(1) put, O(1) get
    * `index <-- hash(key)`
    * `put(key, value): table[index]=value`
    * `get(key): return table[index]`
    * `load factor`: a decimal (percentage) of table occupancy (0.8 is 80% filled table)
* `Collisions` - when two *different* keys hash to the same index, how to retrieve the right value?
    * `Separate chaining` - index of table points to a list-like that stores (key, value) tuples
        * upon collision, iterate the chain
        * worst case: O(n) iteration of a chain
    * `Open addressing` - locate another index (probing) to place the key without creating a separate chaining
        * `Linear probing` - iterate until you find the next available index
        * `Quadratic probing` - search for the next available index via a quadratic polynomial
        * `Double hashing` - search for the next available index via a second hash function
        * Drawback: significant degradation in performance when load factor exceeds 0.7. Resizing requires rehashing!
### Trees
* `Construction`
    * WIP:
    * `Sequential construction`
        ```
        init root as null
        init current as null
        init empty queue
        for each element:
            assign root if unassigned
                assign current as root

            assign current.left if unassigned
                then push current.left
                continue to the next element

            assign current.right if unassigned
                then push current.right
                current = queue.pop()
        ```
* `Traversal`
    * `DFS` - use recursion to dive as deep as possible before checking same level
        * `Preorder` - (root, left, right) | report current node BEFORE both recursals
        * `Inorder` - (left, root, right) | report current node in between both recursals
        * `Postorder` - (left, right, root) | report current node AFTER both recursals
        * `Runtime` - O(n), recursion overhed, no auxiliary
            * O(n) - visit every node
    * `BFS` - use a FIFO queue to traverse same level before diving to next level
        * `Runtime` - O(n), less overhead (no recursion), requires auxiliary queue
            * O(n) - visit every node
            * O(1) - each node you `push()` its two children
            * O(1) - each iteration `pop()` the next node to visit
    * `Usage: DFS vs BFS`
        * Use `DFS` for binary search or a targetted O(logn) run time
        * Use `DFS` for height/depth, leaf problems
        * Use `BFS` for level problems, or checking equality between trees
* `Manipulation`
    * `Insertion`
    * `Deletion`
    * `Search/Find`
    * `Rebalancing`
* `Types`
    * `Full` - each node has 0 or K children
    * `Perfect` - full tree but every leaf at the same level
    * `Complete` - every level filled, but the last level has children to the farthest left
    * `Binary` - each node has [0, 1, 2] children, an n-ary tree where n=2
    * `Binary Search` - values in each node is: 1) greater than or equal to all values in the left subtree and 2) less than to all values in the right subtree
    * `n-ary` - each node has [0...n] children
    * `Trie/digital/radix/prefix` - position within the tree defines the key. Keys are often strings
    * `Red/black`
    * `Splay`
    * `AVL`
### Graphs
* `Representations`
    * `Objects + Pointers`
        ```
        Vertex a = new Vertex(1);
        Vertex b = new Vertex(2);
        Edge edge = new Edge(a,b, 30);
        ```
        * Good for: small graphs, flexibility
        * Bad: requires more explicit maintenace of edges in a datastructure
    * `Matrix`
        ```
        N nodes --> N x N Matrix

        values in matrix are non-zero (1 or weighted) to indicate linkage

        specify directionality with row node -> column node
        ```
        * Good for: dense graphs where nodes are heavily connected, need to check O(1) edge existence
        * Bad: often wasted space, redundant data for undirected graphs, if nodes cannot be self-directed O(n) wasted data guaranteed
        * "Find node's neighbors"
            * O(1) get node
            * O(n) guaranteed search row/column
    * `Adjacency List`
        ```
        N nodes --> size(N) list
        each index is associated with a LinkedList of neighbors

        specify directionality with list[index] -> neighbors

        weighting is maintained in LinkedList i.e. (neighbor, weight) or via a separate LinkedList
        ```
        * Good for: sparse graphs where nodes are not heavily connected
        * Bad: LinkedList node and link overhead, more searching to update undirected links (need to update 2 indices), O(degree) to check edge existence
        * "Find node's neighbors"
            * O(1) get node
            * O(n) *worst case* search LinkedList, sparse graphs are not much of an issue.
            * Proportional to the degree of the node (# of neighbors)
* `Dijkstra`
* `Kruskal's MST`
* `A*`
* `Union Find`
    ```
    find(u): return's the leading parent
    union(u, v): assign the parent of u to be the parent of v

    for each edge specified as (u, v):
        if find(u) == find(v):
            # causes cycle
        else:
            union(u, v)
    ```
    * Determines if an edge causes a cycle
### Array
* Fixed chunks of memory
* Search sorted: O(logn) binary search
* Insert O(n)
* Append O(1)
* Delete O(n) if shift
### LinkedList
* Nodes store value and reference to the next node
* Search: O(n), no binary search
* Insert O(1) with reference to previous
* Append O(1)
* Delete O(1) with reference to previous
### FIFO Queue
```
LinkedList data structure
push(): append to end
pop(): get first element, advance the head
```
* Push(): O(1)
* Pop(): O(1)
### LIFO Stack
```
doubly LinkedList data structure
push(): append to end
pop(): get last element, advance the head "backwards"
```
* Push(): O(1)
* Pop(): O(1)
### Priority Queues
* A semi-ordered binary tree
* Min or Max is the root node
* children are greater than parent
* `Runtimes`
    * Get min/max: O(logn), need to maintain property
    * Insert: O(logn)
        * insert at leaf and push it upward
### Heaps
* Array implementaiton of Priority Queue
* Same performance, minus the tree overhead
*
### Famous NP-complete
* `NP-complete` a subset of `NP-hard` problems that are *solved in polynomial time nondeterministically* but verifiable in polynomial time
* a problem is `NP-complete` if every other problem in NP can be transformed/reduced into the problem in polynomial time
    * i.e. all NP problems are reducible into `NP-complete` in polynomial time
* `Traveling salesman` - "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?"
* `Knapsack problem` - "Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items"
* `Boolean satisfiability` - "determining if there exists an interpretation that satisfies a given Boolean formula. In other words, it asks whether the variables of a given Boolean formula can be consistently replaced by the values TRUE or FALSE in such a way that the formula evaluates to TRUE. If this is the case, the formula is called satisfiable. On the other hand, if no such assignment exists, the function expressed by the formula is FALSE for all possible variable assignments and the formula is unsatisfiable"
* `Hamiltonian path` - "determining whether a Hamiltonian path (a path in an undirected or directed graph that visits each vertex exactly once) in a given graph (whether directed or undirected)"
* `Hamiltonian cycle` - "determining whether a Hamiltonian cycle (a cyclic path in an undirected or directed graph that visits each vertex exactly once) in a given graph (whether directed or undirected)"
* `Subgraph isomorphism` - "two graphs G and H are given as input, and one must determine whether G contains a subgraph that is isomorphic to H. Subgraph isomorphism is a generalization of both the maximum clique problem and the problem of testing whether a graph contains a Hamiltonian cycle, and is therefore NP-complete"
* `Subset sum` - "given a set (or multiset) of integers, is there a non-empty subset whose sum is zero? For example, given the set {−7, −3, −2, 5, 8}, the answer is yes because the subset {−3, −2, 5} sums to zero"
* `Clique` - "finding cliques (subsets of vertices, all adjacent to each other, also called complete subgraphs) in a graph. It has several different formulations depending on which cliques, and what information about the cliques, should be found. Common formulations of the clique problem include finding a maximum clique (a clique with the largest possible number of vertices), finding a maximum weight clique in a weighted graph, listing all maximal cliques (cliques that cannot be enlarged), and solving the decision problem of testing whether a graph contains a clique larger than a given size"
* `Minimum Vertex cover` - "a set of vertices such that each edge of the graph is incident to at least one vertex of the set"
    * "A minimum vertex cover is a vertex cover of smallest possible size"
    * "set of vertices where every edge has at least one endpoint in the vertex cover"
* `Independent set` - "set of vertices in a graph, no two of which are adjacent. That is, it is a set S of vertices such that for every two vertices in S, there is no edge connecting the two. Equivalently, each edge in the graph has at most one endpoint in S"
    * "A maximum independent set is an independent set of largest possible size for a given graph G"
* `Dominating set` - "a subset vertices such that every vertex not in the set is adjacent to at least one member of the set. The domination number γ(G) is the number of vertices in a smallest dominating set for G"
* `Graph coloring` - "is a way of coloring the vertices of a graph such that no two adjacent vertices share the same color; this is called a vertex coloring. Similarly, an edge coloring assigns a color to each edge so that no two adjacent edges share the same color, and a face coloring of a planar graph assigns a color to each face or region so that no two faces that share a boundary have the same color"
### OS / Systems / Concurrency
### Recursion and Induction
* `Recursion`
### Discrete Math
* `Set theory`
    * `union` - all elements between two sets
    * `intersection` - all elements existing in both sets
    * `difference` - elements in existing in the former set but not the latter
    * `subset` - all elements of a subset exist in the superset
* `Probability`
    * P(x) and P(y) = P(x)P(y) if independent
    * P(x | y) = P(x and y) / P(y)
* `Combinations` - given N things how many different ways are there to pick R things
* `Permutations` - given N things how many unique different ways are there to order R things
### System Design
### Development Practices
