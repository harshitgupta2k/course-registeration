Course Registration Application

Overview
This is a Django-based course registration application where users can manage accounts and interact with courses. It uses PostgreSQL as the database, and JWT tokens for user authentication and authorization.


Features:
	Account Management:

		Users can sign up and log in as either students or faculty.

		Faculty members can offer courses and manage them.

		Students can register for available courses.

	Course Management:

		Faculty members can offer courses and see a list of courses they have offered.

		Students can view and register for courses.

	Security:

		The application uses JWT tokens for authentication and authorization.

		Proper validation and error handling mechanisms are implemented for the various endpoints.

Requirements

	You can install the necessary dependencies by running:

	pip install -r requirements.txt

	Make sure your PostgreSQL server is running and a database has been created for the project.

Environment Variables
	This application uses environment variables stored in a .env file to handle sensitive information like database credentials and JWT secret key. Here is the 	structure of the .env file:

	Make sure to replace the placeholder values with actual values for your PostgreSQL setup and secret key.


Project Structure

The project is divided into two Django apps:

	accounts: Handles account management (sign-up, login, logout) for students and faculty.

	courses: Manages course offerings by faculty and course registrations by students.


API Endpoints


Account Management (API: /accounts/api)

	Sign Up

		URL: /accounts/api/sign_up/<user_type>/

		Method: POST

		Payload:

		json

		{
  		"username": "john_doe",
  		"email": "john@example.com",
  		"password": "password123",
  		"confirm_password": "password123"
		}

		Description: Allows users to sign up as either a student or faculty by providing a user_type in the URL. It validates the input data and creates a new 		account.
	
	Login

		URL: /accounts/api/login/<user_type>/

		Method: POST

		Payload:

		json

		{
 		 "email": "john@example.com",
 		 "password": "password123"
		}
		Description: Allows users to log in by providing their email and password. On successful login, a JWT token is returned for authentication.


	Logout

		URL: /accounts/api/logout/

		Method: POST

		Payload: None

		Description: Logs the user out by invalidating the JWT token.


Course Management (API: /courses/api)

Offer a Course (Faculty Only)

	URL: /courses/api/offer/

	Method: GET / POST

	GET Payload: None

	Description: Lists all courses offered by the logged-in faculty member.


	POST Payload:

	json

	{
  		"name": "Course Name"
	}

	Description: Allows the logged-in faculty to offer a new course by providing the course name.


Course Registration (Student Only)

	URL: /courses/api/registration/

	Method: GET / POST

	GET Payload: None

	Description: Lists all courses the logged-in student has registered for.

	POST Payload:

	json

	{
		  "name": "Course Name"
	}

	Description: Allows a student to register for a course by providing the course name.

Mentioned APi endpoints Will work in Browser using Django Rest Framework Default APi View.