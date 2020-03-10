from app.application import create_app
import app.application.sentiment.model.model as model

app = create_app()

if __name__ == "__main__":
	# Model is nearly 120mb. It must be loaded prior to launching the Flask app.
	#model.preload_model()
	app.run(host='0.0.0.0', threaded=False)
