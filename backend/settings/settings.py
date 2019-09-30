import os 


class Environment(object):
    """ Principal configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
#    SQLALCHEMY_DATABASE_URI = if os.getenv('DATABASE_URL') else "sqlite:///example.sqlite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopEnvironment(Environment):
    """ Environment Develop configuration class. """
    DEBUG = True
    CSRF_ENABLED = True


class ProductionEnvironment(Environment):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


app_config = {
    'development': DevelopEnvironment,
    'production': ProductionEnvironment
}
