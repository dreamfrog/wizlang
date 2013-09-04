from flask import *
from actions import *
 
app = Flask(__name__,  static_folder='static', 
            static_url_path='', template_folder='templates')

@app.route('/results.html', methods=['GET', 'POST'])
@app.route('/search/<query>', methods=['GET', 'POST'])
def results(query="Jurassic Park"):
    if request.method == 'POST':
        query = request.form['query']
        quote = str(urllib2.quote(query))
        url = "/search/%s" % quote
        return redirect(url)
    else:
        print 'Query: %s' % query
        for actor in criteria:
            if actor.validate(query):
                print 'Accepted Actor: %s' % actor.name
                reps = actor.run(query)
                break
            else:
                print 'Rejected Actor: %s' % actor.name
        return render_template('results.html', **reps)

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        quote = str(urllib2.quote(query))
        url = "/search/%s" % quote
        return redirect(url)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
