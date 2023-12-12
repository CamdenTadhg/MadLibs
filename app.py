from flask import Flask, request, render_template
from stories import Story, fantasy, romance, scifi, mystery, horror
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

selection = ''

@app.route('/')
def select_story():
    """allow user to select a story to play with"""
    stories = ['fantasy', 'horror', 'mystery', 'romance', 'scifi']
    return render_template("select.html", stories=stories)

@app.route('/form')
def collect_words():
    """display a form to gather madlib input words"""
    selection = request.args["stories"]
    return render_template("form.html", story=eval(selection))

@app.route('/story')
def show_story():
    """display the complete story with form input added"""
    selection = fantasy
    output_story = selection.generate(request.args)
    return render_template("story.html", story=output_story)


#give option to select one of the five stories
#add styles
#validate inputs
#create route for new story page
#create links to new story page
#create form for entering new story
#add new story to story list on input