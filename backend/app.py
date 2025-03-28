from manage import app, db
from flask import abort, send_from_directory, jsonify
from config import UPLOADFLOADER, SERVER_HOST, SERVER_PORT
from blueprints import auth, events

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(events, url_prefix='/events')


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
