male(john).
male(mike).
female(anna).
female(sara).

married(john, anna).
married(mike, sara).

sibling(john, mike).
sibling(anna, sara).

% Rules
brother_in_law(X, Y) :- 
    married(X, Z), sibling(Z, Y);
    sibling(X, Z), married(Z, Y).

sister_in_law(X, Y) :- 
    married(X, Z), sibling(Z, Y); 
    sibling(X, Z), married(Z, Y).

