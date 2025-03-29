from manage import app, db, create_admin_user
from flask import abort, send_from_directory, jsonify
from config import UPLOADFLOADER, SERVER_HOST, SERVER_PORT
from blueprints import auth, events, organizer, user

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(events, url_prefix='/events')
app.register_blueprint(organizer, url_prefix='/organizer')
app.register_blueprint(user, url_prefix='/user')

@app.route('/ping')
def ping():
    return "PolyHackIII", 200


@app.route("/test/drop-db", methods=["POST"])
def drop_db():
    if not app.debug:
        abort(404)
    for table in reversed(db.metadata.sorted_tables):
        db.session.query(table).delete()
    db.session.commit()
    return jsonify({"message": "Destroyed"})


@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(UPLOADFLOADER, filename)


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
    with app.app_context():
        create_admin_user()
