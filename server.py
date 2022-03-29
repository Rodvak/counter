from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'appleapple'

# registers every visit, go line 12 of your HTML
@app.route('/')
def index():
	if 'visit' in session:
		session['visit'] += 1
	else:
		session['visit'] = 0
	if 'counter' in session:
		session['counter'] += 0
	else:
		session['counter'] = 0
	return render_template("index.html")

# session.clear, clears the visits to 0
@app.route('/destroy_session')
def clear():
	session.clear()
	return redirect('/')

@app.route('/sum_two')
def plustwo():
	session['visit'] += 1
	return redirect('/')

@app.route('/sum_one')
def plusone():
	if 'visit' in session:
		session['visit'] += 0
	return redirect('/')
# Removed -1 to counter to work with the SENSEI BONUS,
#It works with the for loop but everytime I click sumbit,
# it adds 1 to visit.
@app.route('/form', methods = ['post'])
def increment_form():
    amount = int(request.form['increment']) 
    session['counter'] += amount
    return redirect('/')

  
if __name__ == "__main__":
    app.run(debug=True)