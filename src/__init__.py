from flask import Flask

# this is the first one that runs 
# initialization happens here 

def create_app():
    app = Flask(__name__)
    
    # import the main page that has the blueprint define this way we access during init
    from .main import main as main_blueprint
    
    # register the blue_print instance that has our main
    app.register_blueprint(main_blueprint)
    
    # connect auth page
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app

