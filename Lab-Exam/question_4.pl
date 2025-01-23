edge(a, 1).
edge(a, 3).
edge(1, 2).
edge(3, 4).
edge(1, 2).
edge(1, 4).
edge(2, 5).

path(X, Y) :- edge(X, Y).
path(X, Y) :- edge(X, Z), path(Z, Y).
