from ..branch import branch
import pdb

class dictree:
    def __init__(self, dictionary):

        self.branches = self.__treefication(dictionary, None, [])
        self.nodes = {current_branch.branch_name: current_branch.nodes for current_branch in self.branches}


    def nbranches(self):
        return len(self.branches)

    def __treefication(self, dictionary, current_node=None, branch_parent=None, branches=[]):
        current_branch = branch({key: "node" if isinstance(dictionary[key], dict) else "leaf" for key in dictionary.keys()},
                                branch_name=current_node, branch_parent=branch_parent)
        # print(current_branch)
        branches.append(current_branch)
        if current_branch.nodes:
            for node in current_branch.nodes:
                if node:
                    branches.extend(self.__treefication(dictionary[node], node, current_branch.branch_name, branches=[]))
        return branches

    def __gen_branch(self, dictionary):
        return branch(dictionary)

    def __str__(self):
        # pdb.set_trace()
        tree=[]
        tree.append(f"{self.branches[0].branch_name}\n|")
        position_map = []
        for current_branch_index in range(0,len(self.branches)):
            current_branch = self.branches[current_branch_index]
            current_position = self.__find_position(current_branch, position_map)
            if current_branch.branch_name != "main branch":
                if current_branch_index + 1 < len(self.branches):
                    if self.branches[current_branch_index - 1].branch_name == current_branch.branch_parent:
                        branch_extender = "|"
                    elif current_branch.branch_parent == "main_branch":
                        branch_extender = "|"
                    else:
                        branch_extender = ""
                else:
                    branch_extender = ""
                if current_position==0:
                    side_branch_extender=""
                else:
                    side_branch_extender="|"
                tree.append(f"{branch_extender}{' '*current_position}{side_branch_extender}")
                tree.append(f"{branch_extender}{' '*current_position}{side_branch_extender}--{current_branch.branch_name}")

            if current_branch.leaves:
                for leaf in current_branch.leaves:
                    if current_position!=0 or current_branch.branch_name != "main branch":
                        leave_position=current_position+2
                    else:
                        leave_position=current_position
                    if current_branch_index+1 < len(self.branches):
                        if self.branches[current_branch_index+1].branch_parent==current_branch.branch_name:
                            branch_extender="|"
                        else:
                            branch_extender=""
                    else:
                        branch_extender=""
                    if leave_position == current_position:
                        leaf_extender=""
                    else:
                        leaf_extender="|"
                    tree.append(f"{branch_extender}{' ' * (leave_position)}{leaf_extender}----{leaf}")


        return "\n".join(tree)

    @staticmethod
    def __find_position(current_branch, position_map):
        position_map.append(current_branch.branch_name)
        if current_branch.branch_parent=="root":
            return 0
        else:
            return position_map.index(current_branch.branch_parent)*2