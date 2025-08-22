#!/usr/bin/env python3
"""Flask app with Babel and mock login for the i18n project.

This module configures Flask-Babel (locale selection via URL or headers),
and mocks a login flow via a query parameter, exposing the user on `g.user`.
The index route renders the '5-index.html' template with gettext IDs.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict, Any

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


# Mock user database table
users: Dict[int, Dict[str, Any]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict[str, Any]]:
    """Retrieve a user dict from the mock DB via `login_as` query param.

    Returns None if the parameter is missing or invalid.
    """
    user_id = request.args.get("login_as")
    if not user_id:
        return None
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request() -> None:
    """Execute before each request to set `g.user` for templates/views."""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """Render the index page using translated strings in the template."""
    return render_template('5-index.html')
