from flask import Flask, Response
import captcha


app = Flask(__name__)


@app.route("/Captcha")
def viewcaptcha():
    c = captcha.getCaptcha()
    return Response(c[0], mimetype="image/jpeg")


if __name__ == "__main__":
    app.run()
