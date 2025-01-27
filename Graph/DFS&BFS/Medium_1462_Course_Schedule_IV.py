# Problem description:
# https://leetcode.com/problems/course-schedule-iv/description/

# We can also use Floyd's or Kahn's algorithm. See the editorial. 
# https://leetcode.com/problems/course-schedule-iv/editorial/
# I will learn those methods later.
# Here I post my DFS and BFS solutions.

# Method 1: DFS
def checkIfPrerequisite1(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    ans = []
    
    # Build the graph by adjacent list.
    g = [[] for _ in range(numCourses)]
    for a,b in prerequisites:
        g[a].append(b)
    
    # dfs function returns True if y is a descendant of x.
    # The set visited will be defined later in the for-loop.
    def dfs(x,y):
        visited.add(x)
        if not g[x]:
            return False
        for son in g[x]:
            if son in visited:
                continue
            if son==y:
                return True
            if dfs(son,y):
                return True
        return False
    # In each iteration, reset the visited set.
    for x,y in queries:
        visited = set()
        ans.append(dfs(x,y))
    return ans

# Time complexity: O(p+(n+p)*m), where p is len(prerequisites), n is the number of Courses, m is len(queries).
# In the worst situation, the graph is a complete directed graph, O(p)~O(n^2).
# So, the worst time complexity is O(n*n*m) 
# Space complexity: O(p+n)~O(n^2+n)~O(n^2). Building the graph takes O(p), visited set takes O(n), dfs takes O(n). 
# To be more precise:
# The space that the dfs recursive stack takes is the maximal depth of the sub-graph with ancestor x.
# In the worst situation, that takes O(n).

#PS: In general, both dfs and bfs take time complexity O(V+E), where V = number_of_vertices, E = number_of_edges.

# Method 2: BFS

def checkIfPrerequisite2(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    ans = []

    g = [[] for _ in range(numCourses)]
    for a,b in prerequisites:
        g[a].append(b)
    
    def bfs(x,y):
        if not g[x]:
            return False
        q = [x]
        visited = {x}
        while q:
            curr = q.pop(0)
            for son in g[curr]:
                if son==y:
                    return True
                if son not in visited:
                    visited.add(son)
                    q.append(son)
        return False

    for x,y in queries:
        ans.append(bfs(x,y))
    return ans

# Time complexity: O(p+(n+p)*m)~O(n*n*m), where p is len(prerequisites), n is the number of Courses, m is len(queries).
# Space complexity: O(p+n)~O(n^2+n)~O(n^2). Building the graph takes O(p), visited set takes O(n), bfs queue takes O(n).
