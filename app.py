from flask import Flask, request, render_template
from stories import Story, fantasy, romance, scifi, mystery, horror
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    """display a form to gather madlib input words"""
    return render_template("form.html", story=fantasy)

@app.route('/story')
def show_story():
    """display the complete story with form input added"""
    output_story = fantasy.generate(request.args)
    print(output_story)
    return render_template("story.html", story=output_story)


#add template inheritance
#give option to select one of the five stories
#add styles
#validate inputs
#create route for new story page
#create links to new story page
#create form for entering new story
#add new story to story list on input