from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

def home(request):
	boards = Review.objects.all()
	boards_names = list()

	for board in boards:
		boards_names.append(board.album)

	response_html = "<br>".join(boards_names)

	return render(request, 'home.html', {'boards': boards})


# Create your views here.
