import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.getenv("APP_SETTINGS", "settings.dev"))

@app.route("/")
def index():
    return {"message": f"Hello from {os.getenv('APP_SETTINGS')}"}

if __name__ == "__main__":
    print ("Hola")
    app.run(debug=True)
