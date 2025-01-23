friend(john, mike).
friend(mike, sara).
friend(sara, anna).

is_friend(X, Y) :- friend(X, Y).
is_friend(X, Y) :- friend(X, Z), is_friend(Z, Y).

