#!/usr/bin/env python3
"""Flask application with basic Babel setup for the i18n project.

This module creates a minimal Flask app, configures the Babel extension with
supported languages, default locale, and timezone, and exposes a single
index route that renders the '1-index.html' template.
"""

from flask import Flask, render_template
from flask_babel import Babel

app: Flask = Flask(__name__)


class Config:
    """Application configuration for available languages and Babel defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Load configuration into the Flask app
app.config.from_object(Config)

# Instantiate Babel at module level as required
babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """Render the index page with a welcoming header."""
    return render_template('1-index.html')
