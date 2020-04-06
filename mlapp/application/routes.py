from flask import Blueprint, jsonify, request
from .model.model import predict
from .errors import error_response
from .models import Question, Sentiment, db


bp = Blueprint('api', __name__)


@bp.route('/sentiment', methods=['POST'])
def get_sentiment():
	data = request.get_json()
	if data is not None and len(data["review"]) > 0:
		prediction = predict(data["review"])
		return jsonify(prediction)
	return error_response(400, 'Review must be at least one character')


@bp.route('/prediction', methods=['POST'])
def add_sentiment():
	data = request.get_json()
	if data is not None:
		sentiment = get_sentiment(data['prediction'], data['submit_correct'], data['submit_incorrect'])
		entry = Sentiment(text=request.form.get('body'), sentiment=sentiment, correct=True)
		db.session.add(entry)
		db.session.commit()


@bp.route('/question', methods=['GET'])
def get_question():
	return jsonify(Question.random())
