from flask import Flask,redirect, url_for, render_template, request
import os
import sys
import Chatbot_GUI 


# sys.path.append(os.path.abspath('/Users/yashgupta/Desktop/chatbot/'))

app=Flask(__name__)
# model = load_model(r'/Users/yashgupta/Desktop/chatbot/chatbot_model.h5')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return Chatbot_GUI.chatbot_response(userText)
    # return str(englishBot.get_response(userText))

if __name__=="__main__":
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(debug=False, host='0.0.0.0', port=port, threaded=False)
	#app.run(debug=True)
