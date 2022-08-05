from django.shortcuts import render
from .models import Vote
from django.db.models import Avg, Count, Min, Sum
# Create your views here.

def index(request):
    return render(request, 'vote.html', {})

#@login_required
def votes(request):
    #text = ("Hello, world. You're at the index.")
    test = Vote.objects.all()
    
    test2 = Vote.objects.values('aspirant__name', 'station__ward').annotate(total=Sum('vcast'))
    print (test)
    print (test2)

    #from django.db.models import Avg, Count
    #Book.objects.filter(name__startswith="Django").annotate(num_authors=Count('authors'))
    #Book.objects.filter(name__startswith="Django").aggregate(Avg('price'))
    #highly_rated = Count('book', filter=Q(book__rating__gte=7))
    #Author.objects.annotate(num_books=Count('book'), highly_rated_books=highly_rated)

    #test = Vote.objects.values('aspirant__name').annotate(Sum('vcast'))
    context = {'test': test, 'test2': test}
    return render(request, 'votes.html', context=context)