from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Inside method")
    time.sleep(3)
    return "Here is the response"


if __name__ =='__main__':

    app.run(host="0.0.0.0", port = 8000, threaded=False )