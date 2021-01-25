import re
from collections import Counter


def _tokenize_sexpr(s):
    tokker = re.compile(r" +|[()]|[^ ()]+")
    toks = [t for t in [match.group(0) for match in tokker.finditer(s)] if t[0] != " "]
    return toks

def _ball(toks, start_index):
    """
    return the end index of the parenthesis expresion.
    """
    counter = 0
    for i, tok in enumerate(toks[start_index:]):
        if tok == "(":
            counter += 1
        elif tok == ")":
            counter -= 1

        if counter == 0:
            return start_index + i + 1

def _unite_tree(toks, inner_label):
    """
    build the tree from the tokens recursivly.
        toks: the tokens we need to parse into a tree structure.
        inner_label: the label of the root.
    """
    if len(toks) == 1:
        return Tree(inner_label, [Tree(toks[0], None)])

    start_index1 = 1
    end_index1 = _ball(toks, start_index1)
    start_index2 = end_index1
    end_index2 = _ball(toks, start_index2)

    a = toks[start_index1 : end_index1]
    left_tree = _unite_tree(a, inner_label)
    b = toks[start_index2 : end_index2]
    right_tree = _unite_tree(b, inner_label)

    return Tree(inner_label, [left_tree, right_tree])

class Tree(object):
    def __init__(self, label, children=None):
        """
        tree object that get:
            label:      for the root node (string of the corresponding word in the tree structure).
            children:   list of [left, right], [child], or none.

        The idea is that for any node in the tree (that not represent a word in the sentance)
        will have children, and all the leafs contain the sords of the sentance.
        """
        self.label = label
        self.children = children

    @staticmethod
    def from_sexpr(string, inner_label):
        toks = _tokenize_sexpr(string)
        if len(toks) < 2 or toks[0] != "(":
            raise RuntimeError('Error Parsing sexpr string')
        return _unite_tree(toks, inner_label)

    def __str__(self):
        if self.children is None: return self.label
        return "[%s %s]" % (self.label, " ".join([str(c) for c in self.children]))

    def isleaf(self):
        return self.children is None

    def leaves_iter(self):
        if self.isleaf():
            yield self
        else:
            for c in self.children:
                for l in c.leaves_iter(): yield l

    def leaves(self):
        return list(self.leaves_iter())

    def nonterms_iter(self):
        if not self.isleaf():
            yield self
            for c in self.children:
                for n in c.nonterms_iter(): yield n

    def nonterms(self):
        return list(self.nonterms_iter())
