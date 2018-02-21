from django.shortcuts import render
from .models import Game 

# Create your views here.
def game_list (request):
	toy= Game.objects.all()
	context = {
		"toy": toy
	}

	return render(request , "list.html" , context)


def game_detail (request, game_id):
	context = {
		"levelup": Game.objects.get(id= game_id)
	}

	return render(request , "detail.html" , context )