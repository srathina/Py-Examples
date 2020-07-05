from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		"author": "RSK",
		"title": "Blog post 1",
		"content": "first post content",
		"Date_posted": "July 5, 2020"
	},
	{
		"author": "Anitha",
		"title": "Blog post 2",
		"content": "second post content",
		"Date_posted": "July 8, 2020"
	}
]

#@ is called decorator
@app.route('/')
@app.route('/home')
def home():
  	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)