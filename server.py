from database import *

@app.route('/')
def mainPage():
    return render_template('new-demo.html')
@app.route('/education')
def edu():
    result_certi = db.session.execute(db.select(Certifcate)).scalars().all()
    return render_template('education.html',items = result_certi)
@app.route('/work')
def work():
    result_work = db.session.execute(db.select(Work)).scalars().all()
    return render_template('work.html',items = result_work)


@app.route('/mobile')
def mobilePage():
    result_mobileApp = db.session.execute(db.select(Mobileapp)).scalars().all()
    return render_template('details.html',items = result_mobileApp)
@app.route('/fullstack')
def fullStack():
    result_fullstack = db.session.execute(db.select(Fullstack)).scalars().all()
    return render_template('details.html',items = result_fullstack)
@app.route('/frontend')
def frontEnd():
    result_frontend = db.session.execute(db.select(Frontend)).scalars().all()

    return render_template('details.html',items = result_frontend)


if __name__ == "__main__":
    # app.secret_key = 'SECRET KEY'

    app.run(debug=True)
