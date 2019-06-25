from app import create_app

app = create_app()
app.run(threaded=True)
