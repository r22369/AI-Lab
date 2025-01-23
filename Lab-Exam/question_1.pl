male(john).
male(mike).
female(anna).
female(sara).

loves(john, anna).
loves(mike, anna).
loves(anna, john).

jealous(X, Y) :-
    loves(X, Z),
    loves(Y, Z),
    X \= Y.
