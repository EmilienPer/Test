import os
from flask import Flask, render_template
app = Flask(__name__)
import git


@app.route('/')
def hello_world():
   sha: "N/A"
   try:
      repo = git.Repo(search_parent_directories=True)
      sha = repo.head.object.hexsha
   except:
      pass
   return render_template('index.html', sha=sha)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='0.0.0.0', port=port)