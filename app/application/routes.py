from flask import Blueprint, render_template, request, redirect, url_for
import requests
import json
from .forms import SentimentPredictionForm


bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@bp.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
	form = SentimentPredictionForm()

	# user submitted prediction feedback
	if (request.form.get('submit_correct') or request.form.get('submit_incorrect')) and form.validate_on_submit():
		sentiment = {'prediction': request.form.get('prediction'),
					 'submit_correct': request.form.get('submit_correct'),
					 'submit_incorrect': request.form.get('submit_incorrect'),
					 'review': request.form.get('body')}
		requests.post("http://localhost:5001/prediction", json=sentiment)
		return redirect(url_for('routes.sentiment', reviewed=True))

	# user submitted review
	if request.form.get('submit_review') and form.validate_on_submit():
		review = {"review": request.form.get('body')}
		response = requests.post("http://localhost:5001/sentiment", json=review)
		if response.status_code == 200:
			form.prediction.data = response.json()
		return render_template('project_sentiment.html', form=form)

	return render_template('project_sentiment.html', form=form, reviewed=request.args.get('reviewed'))


@bp.route('/question', methods=['POST'])
def question():
	''' Returns a random question from the Question database
	'''
	response = requests.get("http://localhost:5001/question")
	question = response.json()
	return (question, 200) if question else 500

