import os
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__) 






@app.route('/')
def index():
	return render_template('index.html')


@app.route('/show',methods=['GET','POST'])
def show(): 
	if request.method == "POST":
		name = request.form['name']
		return render_template('show.html',name=name)
	elif request.method == "GET":
		return redirect(url_for('index'))




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)