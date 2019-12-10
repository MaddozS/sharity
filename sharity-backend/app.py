from app import create_app, create_api

api = create_api()
app = create_app("development", api)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
