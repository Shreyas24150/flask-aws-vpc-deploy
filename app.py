from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Deployed inside Custom VPC by Shreyas"

app.run(host="0.0.0.0", port=80)
