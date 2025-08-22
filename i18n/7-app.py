#!/usr/bin/env python3
"""Flask app with Babel and mock login for the i18n project.

This module configures Flask-Babel (locale and timezone selection) using
custom selectors with the following priority:
 - Locale: URL > user > headers > default
 - Timezone: URL > user > default

It mocks a login flow via a query parameter, exposing the user on `g.user`.
The index route renders the '7-index.html' template with gettext IDs.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict, Any
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    """Resolve locale with priority: URL -> user -> headers -> default.

    1) If `?locale=<code>` is in the query string and supported, use it.
    2) If a user is logged in and has a supported `locale`, use it.
    3) Otherwise, use `Accept-Language` best match among `Config.LANGUAGES`.
    4) Fallback to the default configured locale.
    """
    # 1) URL parameter override
    url_locale = request.args.get("locale")
    if url_locale and url_locale in app.config["LANGUAGES"]:
        return url_locale

    # 2) Logged-in user's preferred locale
    user = getattr(g, "user", None)
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    # 3) Accept-Language header best match
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    # 4) Fallback
    return match or app.config.get("BABEL_DEFAULT_LOCALE", "en")


def get_timezone() -> str:
    """Resolve timezone with priority: URL -> user -> default.

    Validates timezone values using `pytz.timezone`. Falls back to
    the configured default timezone when validation fails or when no
    value is provided.
    """
    # 1) URL parameter override
    url_tz = request.args.get("timezone")
    if url_tz:
        try:
            pytz.timezone(url_tz)
            return url_tz
        except UnknownTimeZoneError:
            pass

    # 2) Logged-in user's preferred timezone
    user = getattr(g, "user", None)
    if user:
        user_tz = user.get("timezone")
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass

    # 3) Fallback to default timezone
    return app.config.get("BABEL_DEFAULT_TIMEZONE", "UTC")


# Initialize Babel with custom locale and timezone selectors
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


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
    return render_template('7-index.html')
