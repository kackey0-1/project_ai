import click
from flask.cli import FlaskGroup

from . import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def main():
    """Management script for the ai_flask_project application."""


if __name__ == "__main__":  # pragma: no cover
    main()
