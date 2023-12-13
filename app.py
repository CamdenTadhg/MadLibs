from flask import Flask, request, render_template
from stories import Story, fantasy, romance, scifi, mystery, horror, stories_dict
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

selection = ''
helperText = {'adjective': 'Describing word. Example: colorful', 'adverb': 'word describing how you do something. Often ends in "ly". Example: quickly','body_part': 'Example: toe', 'building': 'Example: library', 'color': 'Example: blue', 'comparative_adjective': 'describing word ending in "er". Example: faster', 'gerund': 'Verb ending in "ing". Example: running', 'living_thing': 'Example: dog', 'name': 'Example: Austin', 'noun': 'Person, place, or thing. Example: rose', 'past_tense_verb': 'action word that already happend. Often ends in "ed". Example: walked', 'place': 'Example: New York', 'plural_noun': 'More than one person, place, or thing. Example: roses', 'sound': 'Example: screech', 'verb': 'action word. Example: run'}


@app.route('/')
def select_story():
    """allow user to select a story to play with"""
    return render_template("select.html", stories=stories_dict)

@app.route('/form')
def collect_words():
    """display a form to gather madlib input words"""
    selection = request.args["stories"]
    return render_template("form.html", story_option=eval(selection), selection=selection, helperText=helperText)

@app.route('/<selection>')
def show_story(selection):
    """display the complete story with form input added"""
    selected_story = eval(selection)
    output_story = selected_story.generate(request.args)
    return render_template("story.html", story=output_story)

@app.route('/newstory')
def show_story_form():
    """display a form to collection a new story"""
    return render_template("newstory.html")

@app.route('/submitted')
def process_new_story():
    """process new story data and add it to current story list"""
    return render_template("submitted.html")


#add new story to story list on input