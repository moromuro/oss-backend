from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Game

# Create your views here.

def index(request):
  print('index file')
  # TODO filter list to games newer than current date
  # TODO create countdown on html
  # TODO create proper visuals for cards on both html's
  game_list = Game.objects.order_by('-game_date')

  template = loader.get_template('catalog/index.html')
  context = {
    'game_list': game_list
  }
  
  return render(request, 'catalog/index.html', context)

def oneGame(request, game_id):
  print('one game')

  try:
    game = Game.objects.get(id=game_id)
  except Game.DoesNotExist:
    raise Http404('Game does not exists')

  return render(request, 'catalog/game.html', { 'game': game })
