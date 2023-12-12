from flask import Flask, request, render_template
from stories import Story, fantasy, romance, scifi, mystery, horror
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

selection = ''
helperText = {'adjective': 'Describing word. Example: colorful', 'adverb': 'word describing how you do something. Often ends in "ly". Example: quickly','body_part': 'Example: toe', 'building': 'Example: library', 'color': 'Example: blue', 'comparative_adjective': 'describing word ending in "er". Example: faster', 'gerund': 'Verb ending in "ing". Example: running', 'living_thing': 'Example: dog', 'name': 'Example: Austin', 'noun': 'Person, place, or thing. Example: rose', 'past_tense_verb': 'action word that already happend. Often ends in "ed". Example: walked', 'place': 'Example: town', 'plural_noun': 'More than one person, place, or thing. Example: roses', 'sound': 'Example: screech', 'verb': 'action word. Example: run'}

print(helperText['adjective'])


@app.route('/')
def select_story():
    """allow user to select a story to play with"""
    stories = ['fantasy', 'horror', 'mystery', 'romance', 'scifi']
    return render_template("select.html", stories=stories)

@app.route('/form')
def collect_words():
    """display a form to gather madlib input words"""
    print(helperText['adjective'])
    selection = request.args["stories"]
    return render_template("form.html", story=eval(selection), helperText=helperText)

@app.route('/story')
def show_story():
    """display the complete story with form input added"""
    selection = fantasy
    output_story = selection.generate(request.args)
    return render_template("story.html", story=output_story)


#validate inputs and enter notes for word types
#create route for new story page
#create links to new story page
#create form for entering new story
#give option to select one of the five stories
#add new story to story list on input