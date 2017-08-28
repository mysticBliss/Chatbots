from flask import json
from flask import Flask, request 
app = Flask(__name__)

@app.route('/api', methods = ['POST'])
def api():
    if request.headers['Content-Type'] == 'text/plain':
        from rivescript import RiveScript
        bot = RiveScript()
        bot.load_directory("C:\\Users\\staml\\Desktop\\rivescript-p\\eg\\brain")
        bot.sort_replies()
        msg = request.data[0]
        if msg == '/quit':
            quit()
        reply = bot.reply("localuser", msg)
        
        return json.dumps({'response': reply})
        

    elif request.headers['Content-Type'] == 'application/json':
        from rivescript import RiveScript
        bot = RiveScript()
        bot.load_directory("C:\\Users\\staml\\Desktop\\rivescript-p\\eg\\brain")
        bot.sort_replies()
        msg = request.json['message']
        if msg == '/quit':
            quit()
        reply = bot.reply("localuser", msg)   
        
        return json.dumps({'response': reply})

    else:
        return "415 Unsupported Media Type ;)"
      
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=False)