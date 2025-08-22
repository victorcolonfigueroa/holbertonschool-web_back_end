#!/usr/bin/env python3
"""Flask application with Babel locale selection for the i18n project.

This module creates a minimal Flask app, configures the Babel extension with
supported languages, default locale, and timezone, and provides a custom
`get_locale` function that selects the best match from request headers. The
index route renders the '2-index.html' template.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app: Flask = Flask(__name__)


class Config:
    """Application configuration for available languages and Babel defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Load configuration into the Flask app
app.config.from_object(Config)

# Instantiate Babel without app; initialize with locale selector
babel: Babel = Babel()


def get_locale() -> str:
    """Select the best-matching locale from the incoming request.

    Uses the `Accept-Language` header to choose among `Config.LANGUAGES` and
    falls back to the default locale when no match is found.
    """
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    return match or app.config.get("BABEL_DEFAULT_LOCALE", "en")


# Initialize Babel with custom locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Render the index page with a welcoming header."""
    return render_template('2-index.html')
