from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class SentimentPredictionForm(FlaskForm):
	body = TextAreaField("Answer", validators=[DataRequired()])
	submit_review = SubmitField('Review')
	submit_correct = SubmitField('Correct')
	submit_incorrect = SubmitField('Incorrect')
	prediction = HiddenField('Prediction')
