class branch:
    def __init__(self, dictionary, branch_name=None, branch_parent=None):
        if dictionary:
            if not branch_name:
                branch_name="main branch"
            self.branch_name=branch_name
            if not branch_parent:
                branch_parent="root"
            self.branch_parent=branch_parent
            self.nodes = [k for k,v in dictionary.items() if v=="node"]
            if not self.nodes:
                self.nodes=None
            self.leaves = [k for k, v in dictionary.items() if v == "leaf"]
            if not self.leaves:
                self.leaves=None
            self.branch_parent = branch_parent
    def __repr__(self):
        return str({"branch_name": self.branch_name, "branch_parent": self.branch_parent, "nodes": self.nodes, "leaves":self.leaves})