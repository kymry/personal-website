from flask import Blueprint, render_template, request, redirect, url_for
from app.application.sentiment.forms import SentimentPredictionForm
from app.application.sentiment.model.model import predict, get_sentiment


bp = Blueprint('sentiment_routes', __name__)


@bp.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
	form = SentimentPredictionForm()

	# user submitted prediction feedback
	if (request.form.get('submit_correct') or request.form.get('submit_incorrect')) and form.validate_on_submit():
		from app.application.sentiment.models import Sentiment
		from app.application import db
		sentiment = get_sentiment(request.form.get('prediction'),
								  request.form.get('submit_correct'),
								  request.form.get('submit_incorrect'))
		entry = Sentiment(text=request.form.get('body'), sentiment=sentiment, correct=True)
		db.session.add(entry)
		db.session.commit()
		return redirect(url_for('sentiment_routes.sentiment', reviewed=True))

	# user submitted review
	if request.form.get('submit_review') and form.validate_on_submit():
		prediction = predict(request.form.get('body'))
		form.prediction.data = prediction
		return render_template('project_sentiment.html', form=form)

	return render_template('project_sentiment.html', form=form, reviewed=request.args.get('reviewed'))


@bp.route('/question', methods=['POST'])
def question():
	''' Returns a random question from the Question database
	'''
	from app.application.sentiment.models import Question
	question = Question.random()
	return (question, 200) if question else 500

