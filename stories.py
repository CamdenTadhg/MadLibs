"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


fantasy = Story(
    ["living_thing", "name", "adjective", "noun", "noun_2", "gerund", "noun_3", "adjective_2", "gerund_2", "adjective_3", "plural_noun"],
    """Once upon a time, a young {living_thing} named {name} found a {adjective} {noun} in their {noun_2}. Curious, they opened it and discovered a magical {gerund} {noun_3} inside. Together, {name} and the friendly {noun_3} went on {adjective_2} adventures, {gerund_2} the wonders of their {adjective_3} world and making new {plural_noun} along the way."""
)

romance = Story(
    ["adjective", "noun", "name", "name_2", "gerund", "noun_2", "adjective_2", "noun_3", "gerund_2", "past_tense_verb", "adjective_3", "noun_4", "adjective_4"], 
    """In a {adjective} town, a {noun} named {name} liked a girl named {name_2} who loved {gerund} at the {noun_2}. {name} decided to share their {adjective_2} {noun_3} with {name_2}, and they became the best of friends. As they spent more time {gerund_2}, their friendship {past_tense_verb} into a {adjective_3} kind of love that made their {noun_4} {adjective_4} every day."""
)

scifi = Story(
    ["noun", "color", "name", "adjective", "noun", "past_tense_verb", "gerund", "plural_noun", "adjective_2", "plural_noun_2", "past_tense_verb_2", "adjective_3", "gerund_2", "plural_noun_3"], 
    """On the planet Zorba, where the {noun} glowed {color}, a robot named {name} found a {adjective} {noun} in the forest. When they {past_tense_verb} it, a time portal appeared, whisking them to a world filled with {gerund} {plural_noun} and {adjective_2} {plural_noun_2}. {name} made new friends and together they {past_tense_verb_2} the {adjective_3} galaxy, {gerund_2} about the {plural_noun_3} of the universe."""
)

mystery = Story(
    ["adjective", "place", "adjective_2", "name", "plural_noun", "building", "past_tense_verb", "past_tense_verb_2", "adjective_3", "noun", "gerund", "gerund_2"],
    """In the {adjective} town of {place}, a {adjective_2} detective named {name} noticed strange {plural_noun} near the old {building}. Determined to solve the mystery, they {past_tense_verb} the clues and {past_tense_verb_2} a hidden door behind a {adjective_3} bookshelf. Behind the door, {name} found a robber's lair filled with missing {noun}, {gerund} the mystery of the {gerund_2} {noun} in their town."""
)

horror = Story(
    ["name", "adjective", "sound", "noun", "comparative_adjective", "plural_noun_2", "verb", "plural_noun_3", "adverb", "adjective_2", "body_part"], 
    """Late at night, {name} heard {adjective} {sound} coming from their {noun}, but when they opened the {noun}, there was nothing inside. As they tried to go back to sleep, the {sound} grew {comparative_adjective}, and the {plural_noun_2} seemed to {verb} on the {plural_noun_3}. {adverb}, a {adjective_2} hand touched their {body_part}, and {name}'s heart raced as they realized they were not alone in their room."""
)
