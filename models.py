from db import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    """
    User model to store user details.
    Attributes:
        id (int): Unique identifier for each user.
        username (str): Username of the user.
        email (str): Email address of the user.
        password (str): Hashed password for user authentication.
        quizzes (list): Quizzes created by the user.
        results (list): Results of the quizzes taken by the user.
        scores (list): Scores of the quizzes taken by the user.
        is_admin (bool): Flag to indicate if the user is an admin.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    quizzes = db.relationship('Quiz', back_populates='creator', lazy='dynamic')
    results = db.relationship('Result', back_populates='user', lazy='dynamic')
    scores = db.relationship('Score', back_populates='user', lazy='dynamic')
    questions = db.relationship('Question', back_populates='user', lazy='dynamic')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Quiz(db.Model):
    """
    Quiz model to store quiz details.
    Attributes:
        id (int): Unique identifier for each quiz.
        title (str): Title of the quiz.
        description (str): Description of the quiz.
        user_id (int): Foreign key referencing the user who created the quiz.
        creator (User): Relationship to the user who created the quiz.
        questions (list): Questions associated with the quiz.
        results (list): Results of the quiz taken by users.
        scores (list): Scores of the quiz taken by users.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

    # Relationships
    creator = db.relationship('User', back_populates='quizzes')
    questions = db.relationship('Question', back_populates='quiz', lazy='dynamic', cascade="all, delete-orphan")
    results = db.relationship('Result', back_populates='quiz', lazy='dynamic')
    scores = db.relationship('Score', back_populates='quiz', lazy='dynamic')

    def __repr__(self):
        return f'<Quiz {self.title}>'

class Question(db.Model):
    """
    Question model to store question details.
    Attributes:
        id (int): Unique identifier for each question.
        content (str): Content of the question.
        question_text (str): Text of the question.
        user_id (int): Foreign key referencing the user who created the question.
        quiz_id (int): Foreign key referencing the quiz the question belongs to.
        quiz (Quiz): Relationship to the quiz the question belongs to.
        user (User): Relationship to the user who created the question.
        answers (list): Answers associated with the question.
        choices (list): Choices associated with the question.
    """
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    question_text = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

    # Relationships
    quiz = db.relationship('Quiz', back_populates='questions')
    user = db.relationship('User', back_populates='questions')
    answers = db.relationship('Answer', back_populates='question', cascade='all, delete-orphan')
    choices = db.relationship('Choice', back_populates='question')

class Answer(db.Model):
    """
    Answer model to store answer details.
    Attributes:
        id (int): Unique identifier for each answer.
        question_id (int): Foreign key referencing the question the answer belongs to.
        question (Question): Relationship to the question the answer belongs to.
    """
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, ForeignKey('question.id'), nullable=False)

    # Relationships
    question = db.relationship('Question', back_populates='answers')

class Result(db.Model):
    """
    Result model to store quiz results.
    Attributes:
        id (int): Unique identifier for each result.
        score (int): Score obtained in the quiz.
        user_id (int): Foreign key referencing the user who took the quiz.
        quiz_id (int): Foreign key referencing the quiz taken.
        question_id (int): Foreign key referencing the question answered.
        choice_id (int): Foreign key referencing the chosen answer.
        user (User): Relationship to the user who took the quiz.
        quiz (Quiz): Relationship to the quiz taken.
    """
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, ForeignKey('quiz.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='results')
    quiz = db.relationship('Quiz', back_populates='results')

class Score(db.Model):
    """
    Score model to store user scores for quizzes.
    Attributes:
        id (int): Unique identifier for each score.
        user_id (int): Foreign key referencing the user who took the quiz.
        quiz_id (int): Foreign key referencing the quiz taken.
        score (int): Score obtained in the quiz.
        user (User): Relationship to the user who took the quiz.
        quiz (Quiz): Relationship to the quiz taken.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer)

    # Relationships
    user = db.relationship('User', back_populates='scores')
    quiz = db.relationship('Quiz', back_populates='scores')

class Choice(db.Model):
    """
    Choice model to store answer choices for questions.
    Attributes:
        id (int): Unique identifier for each choice.
        text (str): Text of the choice.
        is_correct (bool): Flag indicating if the choice is the correct answer.
        question_id (int): Foreign key referencing the question the choice belongs to.
        question (Question): Relationship to the question the choice belongs to.
    """
    id = Column(Integer, primary_key=True)
    text = Column(String(100), nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=False)

    # Relationships
    question = relationship('Question', back_populates='choices')

