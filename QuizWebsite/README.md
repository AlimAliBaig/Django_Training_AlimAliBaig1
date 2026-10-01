# QuizMaster Django Website

A Django MCQ quiz website with:
- Sign Up
- Sign In
- Logout
- Protected quizzes
- Multiple-choice questions
- Automatic score/percentage/grade
- Question-wise report card
- Student result history
- Django Admin for quizzes/questions/options

## Run

1. Open terminal in this folder.
2. Create/activate a virtual environment.
3. Install dependencies:
   python -m pip install -r requirements.txt
4. Create migrations:
   python manage.py makemigrations
5. Apply migrations:
   python manage.py migrate
6. Create admin:
   python manage.py createsuperuser
7. Start:
   python manage.py runserver

Open:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

## Create a quiz

Admin -> Quizzes -> Add Quiz.
Then add Questions inside the Quiz and add 4 Options to each Question.
Set exactly one Option as "is_correct=True".
