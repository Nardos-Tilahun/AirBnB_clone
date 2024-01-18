0. README, AUTHORS
	
	Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
You should use branches and pull requests on GitHub - it will help you as team to organize your work

1. Be pycodestyle compliant!

	Write beautiful code that passes the pycodestyle checks.

2. Unittests

	All your files, classes, functions must be tested with unit tests

3. BaseModel

	Write a class BaseModel that defines all common attributes/methods for other classes:

4. Create BaseModel from dictionary

	Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

5. Store first object

	Now we can recreate a BaseModel from another one by using a dictionary representation:

6. Console 0.0.1

	Write a program called console.py that contains the entry point of the command interpreter:

7. Console 0.1

	Update your command interpreter (console.py) to

8. First User

	Write a class User that inherits from BaseModel:

9. More classes!

	Write all those classes that inherit from BaseModel:

10. Console 1.0

	Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

11. All instances by class name

	Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().

12. Count instances

	Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().

13. Show

	Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).

14. Destroy
	
	Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).

15. Update

	Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

16. Update from dictionary

	Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

17. Unittests for the Console!

	Write all unittests for console.py, all features!

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:
