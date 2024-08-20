from flask import Flask, redirect, url_for, render_template, request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/pass/<int:score>')
def pass_score(score):
    res=''
    if score>40:
        res="The Examinee is Pass and the score is "+ str(score)
    else:
        res='The Examinee is Fail and the score is '+ str(score)
    exp={'Final Score': score, 'Result': res}
    return render_template('result.html', result=exp)        

@app.route('/fail/<int:score>')
def fail(score):
    return "The examinee is failed and the score is"+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<40:
        result='fail'
    else:
        result='pass_score'
    return redirect(url_for(result,score=marks))

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
        
    res=""
    if total_score>=40:
        res="pass_score" 
    else:
        res='fail' 
    return redirect(url_for(res, score=total_score))


if __name__=='__main__':
    app.run(debug=True)