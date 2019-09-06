from ..branch import branch

class dictree:
    def __init__(self, dictionary):

        self.branches = self.__treefication(dictionary, None, [])
        # print(self.branches)
        self.nodes = [current_branch.nodes for current_branch in self.branches]

    def nbranches(self):
        return len(self.branches)

    def __treefication(self, dictionary, current_node=None, branches=[]):
        current_branch = branch({key: "node" if isinstance(dictionary[key], dict) else "leaf" for key in dictionary.keys()},
                                current_node)
        # print(current_branch)
        branches.append(current_branch)
        if current_branch.nodes:
            for node in current_branch.nodes:
                if node:
                    branches.extend(self.__treefication(dictionary[node], node, branches=[]))
        return branches

    def __gen_branch(self, dictionary):
        return branch(dictionary)

    def __repr__(self):

        tree = f'''
        {self.branches[0].leaves}
        |
        |                                     {self.branches[1].leaves[0]}                 {self.branches[1].leaves[1]}
        |                                     |                                            |
        ---<{self.branches[1].branch_origin}» --------------------------------------------------------------
        '''
        return tree