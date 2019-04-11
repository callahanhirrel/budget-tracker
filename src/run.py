from budget_app import app

# We include this conditional so we can run this script
# directly using Python if we wish, as opposed to using
# environment variables in our virtual environment.
# (i.e. using 'python run.py' instead of
# 'flask run' in terminal/command prompt)
if __name__ == "__main__":
    app.run(debug=True)
