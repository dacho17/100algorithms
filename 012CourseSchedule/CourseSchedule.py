class CourseGraph(object):
    def __init__(self, n , lst):
        self.size = n
        self.mat = self.build_adjacency_matrix(lst)

    def build_adjacency_matrix(self, lst):
        mat = {}
        for pair in lst:
            if pair[1] not in mat:
                mat[pair[1]] = []
            mat[pair[1]].append(pair[0])
        return mat

    def can_be_finished(self):
        route, not_cyclical_cache = set(), set()
        for node in self.mat.keys():    # Here all of the nodes are sent to dfs. Starting edges could have been also detected an only those sent
            if not self.is_acyclical(node, route, not_cyclical_cache):
                return False
        return True

    def is_acyclical(self, node, route, cache):  # DFS algorithm tracking current node and route, as well as nodes from which routes have already been checked
        if node in cache or node not in self.mat:   # node has already been cleared or is a leaf
            return True
        if node in route:
            return False
        
        route.add(node)
        for neighbor in self.mat[node]:
            if not self.is_acyclical(neighbor, route, cache):
                route.remove(node)
                return False
        route.remove(node)

        cache.add(node)
        return True
