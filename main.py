### Integrate HTML, CSS, and JS with Flask

'''

{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments

'''

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/result/<string:res>')
def result(res):
    return res

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        stats = float(request.form['stats'])
        python = float(request.form['python'])
        datascience = float(request.form['datascience'])
        total_score = (science+stats+python+datascience)/4
        
        res = ""
        if total_score >= 50:
            res = "PASS"
        else:
            res = "FAIL"
    return redirect(url_for('result', res=res))

if '__main__' == __name__:
    app.run(debug=True)