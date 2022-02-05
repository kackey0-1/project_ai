from flask import render_template, redirect, url_for


def index():
    return render_template("index.html")


def redirect_to_index(text):
    return redirect("/")
