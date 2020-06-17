from flask import render_template
from app import app, pages

@app.route('/')
def index():
    return "Hello world!"