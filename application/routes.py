from flask import redirect, url_for, request, render_template
from . import app
from . import db
from .models import Company, Frankendama
from .forms import FrankForm

