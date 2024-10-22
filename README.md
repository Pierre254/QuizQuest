QuizQuest Overview
QuizQuest is an engaging, web-based quiz platform developed by Pierre254. It allows users to take quizzes, track their scores, and receive instant feedback. Born out of a passion for interactive learning, QuizQuest is a blend of robust backend technologies and a sleek, responsive design.

Features
User Authentication: Users can register and log in to keep track of their quiz results. Quiz Management: Admins have the capability to create, edit, and delete quizzes. Multiple Choice Questions: Quizzes consist of multiple-choice questions with diverse answer options. Real-time Feedback: Users receive immediate feedback on their quiz performance. Responsive Design: The application is optimized for both desktop and mobile devices.

Technologies Used
Backend:

Flask: For routing, handling HTTP requests, and managing the application’s logic.

SQLAlchemy: ORM for database interaction and model management (e.g., Quiz, Question, Choice, Result).

Flask-Migrate: For seamless database migrations.

Flask-Bcrypt: Ensures secure user authentication through password hashing.

Flask-Login: Manages user sessions and authentication.

Flask-WTF: For form handling with CSRF protection.

Frontend:

HTML, CSS, JavaScript

Database:

SQLite: For storing quiz data, user information, results, and other app-related data.

Version Control:

Git

Installation
To set up QuizQuest locally:

Clone the repository:

bash

Copy
git clone https://github.com/Pierre254/QuizQuest.git
cd QuizQuest
Create a virtual environment:

bash

Copy
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:

bash

Copy
pip install -r requirements.txt
Set up the database:

bash

Copy
flask db upgrade
Run the application:

bash

Copy
flask run
Open your web browser and navigate to http://127.0.0.1:5000.

Usage
Register on the platform to create an account.

Log in with your credentials.

Access available quizzes and start taking them.

Your results will be tracked and displayed after each quiz.

Development Report
Successes:

Implemented key features like user authentication and quiz management.

Challenges:

Faced and overcame issues with model relationships and debugging complex queries.

Addressed routing errors during development.

Areas for Improvement:

Enhance performance through optimization techniques.

Improve user experience with additional features such as progress tracking and more detailed feedback.

Lessons Learned:

Strengthened skills in Flask, SQLAlchemy, and frontend technologies
