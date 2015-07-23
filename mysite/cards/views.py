from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Card


class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_card_list'

    def get_queryset(self):
        """Return the last 20 published cards."""
        return Card.objects.order_by('-created_at')[:20]

class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'


"""def list_cards(request):
    return HttpResponse("You're looking at list_cards ")

def details(request):
    response = "You're looking at the details "
    return HttpResponse(response)
"""