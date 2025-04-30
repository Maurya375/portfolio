from database import *

@app.route('/')
def mainPage():
    return render_template('new-demo.html')

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
@app.route('/workexp')
def workExp():
    return render_template('work.html')

if __name__ == "__main__":
    # app.secret_key = 'SECRET KEY'
    app.run(debug=True)
