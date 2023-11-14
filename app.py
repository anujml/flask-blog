from flask import Flask, render_template
import pymongo

mongodb_url = 'mongodb+srv://Brock1234:Brock1234@cluster0.y5ykvso.mongodb.net/'
myclient = pymongo.MongoClient(mongodb_url)

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html', mongodb_url=mongodb_url)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
