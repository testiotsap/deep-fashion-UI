from flask import Flask , render_template ,request, json
import os
from query.search import get_links

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		try:
			dummyQuery = "Red color half sleeve striped polo neck t-shirt"
			queryResult = get_links(dummyQuery)
			print(queryResult)
			try:
				return render_template('result.html', data = queryResult)					
			except Exception as e:
				return render_template('error.html', msg = queryResult)
		except Exception as e:
			return render_template('error.html', msg = e)
		
	else:
		return render_template('index.html')

# This function is used  to return dummy data for testing UI
def get_json_data():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static", "data/data.json")
	data = json.load(open(json_url))
	return data

if __name__ == '__main__':
   app.run(host= '0.0.0.0',port=5000,debug=True)