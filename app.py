from flask import Flask,render_template,request

app = Flask(__name__) 




@app.route('/')
def index():
	return render_template('index.html')


@app.route('/show',methods=['GET','POST'])
def show(): 
	name = request.form['name']
	if request.method == "POST":
		return render_template('show.html',name=name)
	else: 
		return render_template('spoilers.html')




if __name__ == "__main__":
	app.run(debug=True)