#!/usr/bin/env python3
"""Flask application with Babel locale selection for the i18n project.

This module creates a minimal Flask app, configures the Babel extension with
supported languages, default locale, and timezone, and provides a custom
`get_locale` function that selects the best match from request headers. The
index route renders the '3-index.html' template with gettext IDs.
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
    """Resolve locale from URL parameter, then headers, else default.

    Priority:
    1) If `?locale=<code>` is in the query string and supported, use it.
    2) Otherwise, use `Accept-Language` best match among `Config.LANGUAGES`.
    3) Fallback to the default configured locale.
    """
    # 1) URL parameter override
    url_locale = request.args.get("locale")
    if url_locale and url_locale in app.config["LANGUAGES"]:
        return url_locale

    # 2) Accept-Language header best match
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    # 3) Fallback
    return match or app.config.get("BABEL_DEFAULT_LOCALE", "en")


# Initialize Babel with custom locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Render the index page using translated strings in the template."""
    return render_template('4-index.html')
