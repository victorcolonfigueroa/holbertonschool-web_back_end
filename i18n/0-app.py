#!/usr/bin/env python3
"""Basic Flask application module for the i18n project.

 This module creates a minimal Flask application with a single index route
 that renders the '0-index.html' template.
 """

from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """Render the index page with a welcoming header."""
    return render_template('0-index.html')
