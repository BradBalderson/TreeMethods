This repository stores a basic implementation for creating a neighbour joining tree from a given distance or similarity matrix.

Generating a distance matrix (A good way to do this is to use sklearn.DistanceMetrics with real data):

    from sklearn.neighbors import DistanceMetric

    dist = DistanceMetric.get_metric('euclidean')
    X = [[0, 1, 2],
         [3, 4, 5],
         [2, 3, 1],
         [0, 2, 1]]
    dist_mat = dist.pairwise(X)

Now that we have our distance matrix, we can now use it to construct a neighbour joining tree, 
giving some labels for the different samples:

    import numpy
    import TreeMethods.TreeBuild as TB

    tree = TB.njTree(dist_mat, numpy.array(['A', 'B', 'C', 'D']))

We can then use ete3 to construct this into a tree object:

    from ete3 import Tree

    tree = Tree(tree)
    print(tree)

       /-B
      |
      |   /-D
    --|--|
      |   \-A
      |
       \-C
