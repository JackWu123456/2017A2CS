

WHILE  There are Staffs

	CALL ReadSalary()

	IF Salary > 50 

		THEN	

			IF Salary >= 90 

				THEN

					Role = Project Manager

				ELSE 

					Role = Lead Developer

			ENDIF

		ELSE

			Role = Manager

	ENDIF

ENDWHILE




Task 1.4

        Salary > 50

     FALSE             TRUE                   

Assign Manager       Salary >=90   

           	FALSE                    TRUE

              Salary >70          Assign Project Manager 。

       FALSE                    TRUE 

Assign Lead Developed 。    Assign Consultant 。




Task 1.5

IF Salary >= 90 

	THEN 

		Role = ProjectManager 

	ELSE 

		IF Salary > 70 

			THEN 

				Role = Consultant 

			ELSE 

				Role = LeadDeveloper 

		ENDIF 

ENDIF




 

Task 1.6




def determinerole(salary):

    if salary>50:

        if salary>70:

            if salary>=90

                role = 'projectmanager'

            else:

                role =  'consultant'

        else:

            role =  'leaddeveloper'

    else:

        role =  'manager'
