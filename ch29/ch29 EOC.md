1

a. 

cityIn(london,uk).
iVisited(strabourg).
b.

chile, argentina
c.

countriesIVisited(Country) :-
	iVisited(City),cityIn(City,Country).
2

a. i. Clause 01
ii. Clause 15

b. i. ii. iii.

Who = jack.

False.

False.
c. i.

qualifiedDriver(Driver,car).
ii.

theoryOnly(X) :-
	passedTheoryTest(X),not(passedDrivingTest(X)).
d.

C11 hasLicence(mike). /* - True */ 
C01 minimumAge(car,L). /* - True, L = 18. */ 
C05 age(mike,A). /* - True, A = 17. */ 
C15 A >= L. /* - False. */ 

/* So */ False.