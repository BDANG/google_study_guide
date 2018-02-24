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
### Array
* Fixed chunks of memory
* Search sorted: O(logn) binary search
* Insert O(n)
* Append O(1)
* Delete O(n) if shift
### LinkedList
### FIFO Queue
```
LinkedList data structure
push(): append to end
pop(): get first element, advance the head
```
### LIFO Stack
```
doubly LinkedList data structure
push(): append to end
pop(): get last element, advance the head "backwards"
```
### Priority Queues
* Min or Max is the root node
* children are greater than parent
* `Runtimes`
    * Get min/max: O(logn), need to maintain property
    * Insert: O(logn)
        * insert at leaf and push it upward
### Heaps
* Array implementaiton of Priority Queue
* Same performance, minus the tree overhead
### Famous NP-complete
### OS / Systems / Concurrency
### Recursion and Induction
### Discrete Math
### System Design
### Development Practices
