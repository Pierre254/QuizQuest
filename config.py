import os

class Config:
    """
    Configuration class for setting Flask app configurations.
    """
    # Secret key for securing sessions and forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6ab3373251476733f91574db2a9fddef'

    # Database URI for SQLAlchemy
    # Default to SQLite for local development; override with DATABASE_URL in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # Disable modification tracking to save memory and improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Example configuration options for mail server (uncomment if needed)
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # Example configuration for pagination (if needed)
    # POSTS_PER_PAGE = 10

