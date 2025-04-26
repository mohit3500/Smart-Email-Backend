from flask import Flask, request, jsonify
from email_generator import generateEmail

app = Flask(__name__)


@app.route("/generate-email", methods=["POST"])
def email_api():
    data = request.get_json()
    subject = data.get("subject")
    generate_text = generateEmail(subject)
    return jsonify({"generated_email": generate_text})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
