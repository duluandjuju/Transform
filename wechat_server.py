from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def WechatInitial():
    if request.method == "GET":
        print("auth req coming")
        data = request.args
        token = "askjncy19uAAklkn0kkO00012"
        signature = data.get("signature", "")
        timestamp = data.get("timestamp", "")
        nonce = data.get("nonce", "")
        echostr = data.get("echostr", "")
        s = [timestamp, nonce, token]
        s.sort()
        s = "".join(s)
        if(hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)