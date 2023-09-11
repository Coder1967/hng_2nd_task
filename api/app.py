from flask import Flask, jsonify, request
from flask_cors import CORS
import models
from api.views import app_views

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(app_views)

@app.errorhandler(404)
def handle_404(e):
    """ handles a 404 httpexception"""
    return jsonify({'error': "Not found"}), 404

@app.errorhandler(400)
def handle_400(e):
    """handles code 400 httpexception """
    message = e.description
    return jsonify({'error': message}), 400



@app.teardown_appcontext
def teardown_db(exception):
    """ closes off session with database"""
    models.storage.close()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", threaded=True)
