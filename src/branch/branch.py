class branch:
    def __init__(self, dictionary, branch_origin=None):
        if dictionary:
            if not branch_origin:
                branch_origin="root"
            self.branch_origin=branch_origin
            self.nodes = [k for k,v in dictionary.items() if v=="node"]
            if not self.nodes:
                self.nodes=None
            self.leaves = [k for k, v in dictionary.items() if v == "leaf"]
            if not self.leaves:
                self.leaves=None

    def __repr__(self):
        return str({"branch_origin": self.branch_origin, "nodes": self.nodes, "leaves":self.leaves})