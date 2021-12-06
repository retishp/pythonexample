import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

@app.route('/list', methods=['GET'])
def userlist():
  return userlist()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

def userlist():
  usrArray = ['tom', 'joe', 'alice']
  for x in range(10):
      print(usrArray[x])