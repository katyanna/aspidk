from django.shortcuts import render
from django.http import HttpResponse
from .models import Concept
import random
import pdb

def index(request):
    min = Concept.objects.first().id
    max = Concept.objects.last().id
    rand_id = random.randint(min, max)
    concept = Concept.objects.get(id=rand_id)
    context = {'concept': concept,}
    return render(request, 'cards/index.html', context)
