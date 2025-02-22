import genanki

# Note



# Model

my_model = genanki.Model(
  7894561230,
  'Simple Model',
  fields=[
    {'name': 'AnswerKey'},
    {'name': 'Question'},
    {'name': 'AnswerChoices'},
    {'name': 'CorrectAnswerText'},
  ],
  templates=[
    {
      'name': 'Card1',
      'qfmt': '{{Question}}<hr id="answer-choices">{{AnswerChoices}}',
      'afmt': '{{Question}}<hr id="answer-text">
