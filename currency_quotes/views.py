from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import random

from . import util

def index(request):

	if request.method == 'GET':
		return render(request, "currency_quotes/index.html", {
			"entries": util.list_entries()
		})
