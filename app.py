import datetime
import os
import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for

load_dotenv()

app = Flask(__name__)

# mongodb_url = 'mongodb+srv://Brock1234:Brock1234@cluster0.y5ykvso.mongodb.net/microblog'
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
app.db = client.microblog

entries = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():
  if request.method == "POST":
    entry_content = request.form.get('content')
    formatted_date = datetime.datetime.now().strftime("%Y-%m-%d")
    app.db.entries.insert_one({
        'content': entry_content,
        'date': formatted_date
    })

  entries_with_date = [
      (entry['content'], entry['date'],
       datetime.datetime.strptime(entry['date'], '%Y-%m-%d').strftime('%b %d'))
      for entry in app.db.entries.find({})
  ]
  return render_template('home.html', entries=entries_with_date)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
