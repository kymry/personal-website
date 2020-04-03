from flask import Blueprint, render_template
from . import bp

@bp.errorhandler(404)
def page_not_found_error(error):
    return render_template('404.html'), 404


@bp.errorhandler(500)
def internal_error(error):
    return render_template('404.html'), 500