from flask import Flask,render_template,request,jsonify
import os, json

fi = Flask(__name__)
#path = os.getcwd()
#html_path = path + "/templates/calculator.html"

@fi.route('/')
def index():
	return render_template("calculator_jquery.html")

@fi.route('/output',methods=['GET','POST'])
def calculation():
        res = {}
	if request.method == 'POST':
                data = json.loads(request.data)
                res['output'] = eval(data['input'])
		return jsonify(res)

if __name__ == '__main__':
	fi.run(host ="0.0.0.0")
	
