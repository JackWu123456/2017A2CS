capitalCity(paris).
capitalCity(berlin).
capitalCity(cairo).

brother(A,B) :- 
	parent(P,A),parent(P,B),male(A),not(A=B).

sister(A,B) :- 
	parent(P,A),parent(P,B),female(A),not(A=B).

son(A,B) :- 
	parent(B,A),male(A).

daughter(A,B) :- 
	parent(B,A),female(A).

married(A,B) :- 
	parent(A,K),parent(B,K),not(A=B).

ancestor(A,B) :- 
	parent(A,B);
	parent(A,T),ancestor(T,B).

factorial(0,1).
factorial(N,F) :- 
	X is N-1,
	factorial(X,Y),
	F is N * Y.

writeList([]).
writeList([H|T]) :-
	write(H),nl,writeList(T).