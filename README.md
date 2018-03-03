# Review Guide for Google's Technical Phone Interview
#### by Brian Dang
###


(**Example code requires Python3**)
###


### Algorithms
* `Dynamic Programming` - technique which is usually based on a recurrent formula and one (or some) starting states. A sub-solution of the problem is constructed from previously found ones. DP solutions have a polynomial complexity which assures a much faster running time than other techniques like backtracking, brute-force etc
    *  find a state for which an optimal solution is found and with the help of which we can find the optimal solution for the next state
    * recurrent relation, which makes a connection between a lower and a greater state
    * define a "state" which represents a sub-problem and thus we have to find a solution for it
    * in most cases the states rely on lower states and are independent from greater states
### Sorting
* `Mergesort`
    * Divide and conquer, recursively divide until 1-element array
    * Recursively build up the splits in sorted order. Pick the smaller element between two subarrays
    * `Runtime`: O(nlogn) worst case
    * `Space`: O(n) auxiliary
    * Stable sort
* `Quicksort`
    ```
    partition(list, left, right, pivot)
        while left less than or equal to right
            increment left till misplaced value
            decrement right till misplaced value

            if left value less than or equal to right value
                swap(left value, right value)
                increment left
                decrement right

        return left

    sort(list, left, right)
        if left greater or equal to right
            return

        select pivot value
        i = partition(list, left, right, pivot)
        sort(list, left, i-1)
        sort(list, i, right)
    ```
    * Select a pivot and sort elements to the right or left of the pivot
    * `Runtime`: O(n^2) worst case, O(nlogn) average
    * `Space`: O(1) in place or O(n) auxiliary
    * NOT STABLE
### Hashtables
* `Overview`
    * A symbol table (key-value)
    * `put(key, value)`: O(1)
    * `get(key)`: O(1)
    * `delete(key)`: O(1)
    * `resize()`: O(K) -- each key needs to be put() again
        ```
        index = hash(key)
        put(key, value): table[index]=value
        get(key): return table[index]
        delete(key): table[index] = None
        ```
    * `load factor`: a decimal (percentage) of table occupancy (0.8 is 80% filled table)
* `Collisions` - when two *different* keys hash to the same index, how to retrieve the right value?
    * `Separate chaining` - index of table points to a list-like that stores (key, value) tuples
        * upon collision, iterate the chain
        * worst case: O(n) iteration of a chain
        * resizes less often since chains can be arbitrarily long but avoiding resizes causes more degradation to O(n)
    * `Open addressing` - locate another index (probing) to place the key without creating a separate chaining
        * `Linear probing` - increment linearly (often +1) until you find the next available index
        * `Quadratic probing` - search for the next available index via a quadratic polynomial, avoids clustering (where clustering increases collisions for new keys)
            ```
            index = hash(key)
            probe = 0
            A = constant (!=0)
            B = constant

            until non occupied index:
                searchIndex = (index + probe^2*A + probe*B) mod size
                probe++
            ```

        * `Double hashing` - search for the next available index via a second hash function, avoids repeated collisions that occurs in linear/quadratic. second hash function != size
            ```
            index = hash1(key)
            iterator = 0
            until non occupied index:
                searchIndex = (index + iterator*hash2(key)) mod size
                iterator++
            ```
        * Drawback: significant degradation in performance when load factor exceeds 0.7. Resizing requires rehashing!
### Trees
* `Construction`
    * WIP:
    * `Sequential Construction`
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
    * `Generic Binary Search Tree Construction`
        ```
        init a root with the first value
        for every remaining value:
            bst_insert(root, value)

        bst_insert(root, value):
            base cases (root.left/root.right is None for the correct branch)

            if value <= root.value:
                bst_insert(root.left, value)
            else:
                bst_insert(root.right, value)
        ```
    * `Preorder Binary Search Tree Construction`
        ```
        def recurse(numbers, parent):
            if numbers is empty:
                return parent

            rootvalue = numbers.pop(0)

            find index with element greater than root value

            parent = Node(rootvalue)
            parent.left = recurse(numbers[:rightIndex], parent)
            parent.right = recurse(numbers[rightIndex:], parent)

            return parent

        root = recurse(numbers, None)
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
    ```
    init empty heap
    init parent array with None's for each vertex
    parent[start] = -1
    init empty visited set

    init vertex = source vertex
    init currentWeight = 0

    init found = False

    while size of visited not equal to number of vertices:
        if vertex == sink/target vertex:
            found = True
            break

        if vertex not visited:
            mark vertex visited
            for each neighbor, weight:
                if parent[neighbor] == None:
                    parent[neighbor] = vertex
                heap.push((currentWeight, neighbor))

        if heap not empty:
            (currentWeight, vertex) = heap.pop()
        else:
            break

    if found:
        parse the parent array for path
        return path, currentWeight
    else:
        return None, -1

    ```
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
* Append O(1) with reference to the end
* Delete O(1) with reference to previous
### FIFO Queue
```
LinkedList data structure
push(): append to end
pop(): get head value, head = head.next
```
* Push(): O(1)
* Pop(): O(1)
### LIFO Stack
```
doubly LinkedList data structure
push(): init new_head, new_head.next = old_head
pop(): get head value, head = head.next
```
* Push(): O(1)
* Pop(): O(1)
### Priority Queues
* More of an abstract datatype:
    * Get min/max, peek(): O(1)
    * Remove min/max pop(): O(logn), maintain property
    * Insert: O(logn), insert at leaf and push upward
* A semi-ordered binary tree
* Min or Max is the root node
    * Min PQ: children are greater than or equal to parent
    * Max PQ: children are less than or equal to parent
* Pushing up, swimming
    ```
    current = last index
    while current has parent and parent value > current value:
        swap(parentIndex, currentIndex)
        current = parent(current)
    ```
* Pushing down, sinking
    ```
    current = 0
    while current has left:
        smallerChildIndex = leftchildIndex(current)
        if current has right and rightchild(current) < leftchild(current):
            smallerChildIndex = rightchildIndex(current)

        if item[current] < item[smallerChildIndex]:
            break
        else:
            swap(current, smallerChildIndex)
        current = smallerChildIndex
    ```
### Heaps
* Array implementaiton of Priority Queue
* Same performance, minus the tree overhead
* Relations
    ```
    parent(i) = array[floor of (i-1)/2]
    left_child(i) = array[2*i + 1]
    right_child(i) = array[2*i + 2]
    ```
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
* `Processes` - an instance of a computer program being actively executed, code and current state (memory)
* `Threads` - a lightweight process, exist as a component of a `process`, executed concurrently with shared memory and address space, maintain less state information because it is handled by parent `process`, context switching between `threads` is faster than `processes`
* `Concurrency` - computations from different threads are interleaved instead of executed sequentially
    * `Issues` - need to ensure the correct sequencing of the interactions or communications between different computational executions, and coordinating access to resources that are shared among executions. debugging can be difficult as concurrent execution is nondeterministic
        * `race condition` - output is dependent on the order of execution, arises from interleaving critcal sections that require mutual exclusion
            * avoidance: locking critical sections such that only one thread has access to it for the entire execution of the section
        * `deadlock` - a state where each member of a group is waiting for some other member to complete an action. no active execution
            * avoidance (pick one:):
                * remove *mutual exclusion* but impossible if resource cannot be spooled. spooled resources can still cause deadlock. non-blocking synchronization
                * remove hold and wait by requiring processes to request all the resources they will need before starting up (or before embarking upon a particular set of operations). This advance knowledge is frequently difficult to satisfy and, in any case, is an inefficient use of resources. Or require processes to request resources only when it has none. Thus, first they must release all their currently held resources before requesting all resources it needs. This too is often impractical. Resources may be allocated and remain unused for long periods. Also, a process requiring a popular resource may have to wait indefinitely
                * allow premption, difficult or impossible because a process might need a resource for a long time
                * avoid circular waits include disabling interrupts during critical sections and using a hierarchy to determine a partial ordering of resources
            * detection: observe the state (no progress); each process has locked and/or currently requested are known to the resource scheduler of the operating system
            * resolution: abort 1 process (but lose partial computations), resource preemption
        * `livelock` - "similar to a deadlock, except that the states of the processes involved in the livelock constantly change with regard to one another, none progressing" like the hallway jiggle
            * a risk with some algorithms that detect and recover from deadlock. If more than one process takes action, the deadlock detection algorithm can be repeatedly triggered
            * avoidance: ensuring that only one process (chosen arbitrarily or by priority) takes action
        * `resource starvation` - a process is perpetually denied necessary resources to process its work
            * caused by an overly simplistic scheduling algorithm. For example, if a (poorly designed) multi-tasking system always switches between the first two tasks while a third never gets to run, then the third task is being starved of CPU time
            * avoidance: ensure a scheduler allows equal sharing of CPU time, ensure equal access to resources?
    * `Modern concurrency constructs (cores)` - a single computing component with two or more independent processing units called cores, which read and execute program instructions.[1] The instructions are ordinary CPU instructions (such as add, move data, and branch) but the single processor can run multiple instructions on separate cores at the same time, increasing overall speed for programs amenable to parallel computing
        * implements multiprocessing in a single physical package
        * gained by the use of a multi-core processor depends very much on the software algorithms used and their implementation. In particular, possible gains are limited by the fraction of the software that can run in parallel simultaneously on multiple cores
* `Locks` - allows only one thread to access a locked code (critical region), not shared with other processes, also a binary semaphore
* `Mutexes` - same as a lock, but shared across processes
* `Semaphore` - like a lock, but can allow multiple threads to access the locked code
* `Monitors` - synchronization construct that allows threads to have both mutual exclusion and the ability to wait (block) for a certain condition to become true
    * have a mechanism for signaling other threads that their condition has been met
    * A monitor consists of a mutex (lock) object and condition variables. A condition variable is basically a container of threads that are waiting for a certain condition. Monitors provide a mechanism for threads to temporarily give up exclusive access in order to wait for some condition to be met, before regaining exclusive access and resuming their task
    * Another definition of monitor is a thread-safe class, object, or module that uses wrapped mutual exclusion in order to safely allow access to a method or variable by more than one thread.
* `Context switching` - storing the state of a process or of a thread, so that it can be restored and execution resumed from the same point later. This allows multiple processes to share a single CPU, and is an essential feature of a multitasking operating system
    * context switch can also occur as the result of an interrupt, such as when a task needs to access disk storage, freeing up CPU time for other tasks. Some operating systems also require a context switch to move between user mode and kernel mode tasks
    * usually computationally intensive, and much of the design of operating systems is to optimize the use of context switches
    * saving and loading registers and memory maps, updating various tables and lists
    * context switching threads is often quicker as less saving/loading data
* `Scheduling` - method by which work specified by some means is assigned to resources that complete the work. The work may be virtual computation elements such as threads, processes or data flows, which are in turn scheduled onto hardware resources such as processors, network links or expansion cards
    * The main purposes of scheduling algorithms are to minimize resource starvation and to ensure fairness amongst the parties utilizing the resources
    * Does one of the following: maximizing throughput (amount of work per time unit), minimizing wait time, minimizing latency, maximizing fairness
    * preemptive scheduler: decides which process to run, when to stop, and which is next
    * `long term scheduling` - decides which jobs or processes are to be admitted to the ready queue (in main memory); when an attempt is made to execute a program;
        * dictates what processes are to run on a system, and the degree of concurrency to be supported at any one time
        * Long-term scheduling is also important in large-scale systems such as batch processing systems, computer clusters, supercomputers, and render farms
    * `medium term scheduling` - removes processes from main memory and places them in secondary memory or vice versa, which is commonly referred to as "swapping out" or "swapping in"
        * decide to swap out a process which has not been active for some time, or a process which has a low priority, or a process which is page faulting frequently, or a process which is taking up a large amount of memory in order to free up main memory for other processes, swapping the process back in later when more memory is available, or when the process has been unblocked and is no longer waiting for a resource
    * `short term scheduling` - decides which of the ready, in-memory processes is to be executed (allocated a CPU) after a clock interrupt, an I/O interrupt, an operating system call or another form of signal
        * makes scheduling decisions much more frequently than the long-term or mid-term schedulers – a scheduling decision will at a minimum have to be made after every time slice, and these are very short
        * can be preemptive, implying that it is capable of forcibly removing processes from a CPU when it decides to allocate that CPU to another process, or non-preemptive (also known as "voluntary" or "co-operative"), in which case the scheduler is unable to "force" processes off the CPU
    * `FIFO` - simply queues processes in the order that they arrive in the ready queue
        * scheduling overhead minimal with respect to context switches
        * throughput can be low if long processes queued before short processes
        * no starvation, each process gets executed
        * turnaround time, waiting time, and response time can be long if long processes queued before short processes
        * no prioritization -- likely misses deadlines
    * `Earliest Deadline First` - queue will be searched for the process closest to its deadline, which will be the next to be scheduled for execution
    * `Shortest remaining time first` - arranges processes with the least estimated processing time remaining to be next in the queue. This requires advanced knowledge or estimations about the time required for a process to complete
        * If a shorter process arrives during another process' execution, the currently running process is interrupted (known as preemption), dividing that process into two separate computing blocks. This creates excess overhead through additional context switching. The scheduler must also place each incoming process into a specific place in the queue, creating additional overhead
        * This algorithm is designed for maximum throughput in most scenarios
        * Waiting time and response time increase as the process's computational requirements increase. Since turnaround time is based on waiting time plus processing time, longer processes are significantly affected by this. Overall waiting time is smaller than FIFO, however since no process has to wait for the termination of the longest process
        * No particular attention is given to deadlines, the programmer can only attempt to make processes with deadlines as short as possible
        * Starvation is possible, especially in a busy system with many small processes being run
        * should have at least two processes of different priority
    * `Shortest job first?`
    * `Fixed priority preemptive` - fixed priority rank to every process, and the scheduler arranges the processes in the ready queue in order of their priority. Lower-priority processes get interrupted by incoming higher-priority processes
        * Overhead is not minimal, nor is it significant
        * FPPS has no particular advantage in terms of throughput over FIFO scheduling
        * If the number of rankings is limited, it can be characterized as a collection of FIFO queues, one for each priority ranking. Processes in lower-priority queues are selected only when all of the higher-priority queues are empty
        * Waiting time and response time depend on the priority of the process. Higher-priority processes have smaller waiting and response times
        * Deadlines can be met by giving processes with deadlines a higher priority
        * Starvation of lower-priority processes is possible with large numbers of high-priority processes queuing for CPU time
    * `Round Robin` - The scheduler assigns a fixed time unit per process, and cycles through them. If process completes within that time-slice it gets terminated otherwise it is rescheduled after giving a chance to all other processes
        * involves extensive overhead, especially with a small time unit
        * Balanced throughput between FCFS/ FIFO and SJF/SRTF, shorter jobs are completed faster than in FIFO and longer processes are completed faster than in SJF
        * Good average response time, waiting time is dependent on number of processes, and not average process length
        * Because of high waiting times, deadlines are rarely met in a pure RR system
        * Starvation can never occur, since no priority is given. Order of time unit allocation is based upon process arrival time, similar to FIFO
        * If Time-Slice is large It becomes FCFS /FIFO or If it is short then it becomes SJF/SRTF
    * `Multilevel queue` - for situations in which processes are easily divided into different groups. For example, a common division is made between foreground (interactive) processes and background (batch) processes. These two types of processes have different response-time requirements and so may have different scheduling needs
### Recursion and Induction
* `Recursion`
* `Backtrack`
* `Induction`
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
