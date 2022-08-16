from django.shortcuts import render
from .models import Vote, Aspirant, Seat, Upload
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import VoteForm
from django.contrib import messages
# Create your views here.

def index(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'index.html')

def about(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'about.html')

def service(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'service.html')

def team(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'team.html')

def contact(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'contact.html')

def cert(request):
     #test = Vote.objects.all()
     #context = {'test': test, 'test2': test}
     return render(request, 'cert.html')
     
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated() and not request.user.is_active:
            logout(request)
        # auth.logout(request)
    return redirect('/login')





# def vote(request):
#      submitted = False
#      if request.method == 'POST':
#          form = VoteForm(request.POST)
#          if form.is_valid():
#              form.save()
#              # assert False
#              return redirect('/')
#              #HttpResponseRedirect('/?submitted=True')
#      else:
#          form = VoteForm()
#          if 'submitted' in request.GET:
#              submitted = True
#      return render(request, 
#          'svote.html', 
#          {'form': form, 'submitted': submitted}
#         )
# def vote(request):
#     form = VoteForm
#     if request.method == 'POST':
#         form = VoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Vote Has Been Sent')
#             return redirect('/')
#     return render(request, 'form.html', {'form': form})

# def index(request):
#     test = Vote.objects.all()

#     current_user = request.user
#     print (current_user.id)
#     context = {'test': test, 'test2': test}
#     return render(request, 'form.html', context=context)

# #def vote(request):
#  #   test = Vote.objects.all()
#   #  context = {'test': test, 'test2': test}
#    # return render(request, 'table.html', context=context)
# def index3(request):
#     return render(request, 'index3.html', {})
# def index4(request):
#     return render(request, 'index4.html', {})
# def index6(request):
#     return render(request, 'index6.html', {})
# #@login_required
# def votes(request):
#     #text = ("Hello, world. You're at the index.")
#     test = Vote.objects.all()
#     test2 = Vote.objects.values('aspirant__name', 'station__ward').annotate(total=Sum('vcast'))

#     print (test)
#     print (test2)

#     #from django.db.models import Avg, Count
#     #Book.objects.filter(name__startswith="Django").annotate(num_authors=Count('authors'))
#     #Book.objects.filter(name__startswith="Django").aggregate(Avg('price'))
#     #highly_rated = Count('book', filter=Q(book__rating__gte=7))
#     #Author.objects.annotate(num_books=Count('book'), highly_rated_books=highly_rated)

#     #test = Vote.objects.values('aspirant__name').annotate(Sum('vcast'))
#     context = {'test': test, 'test2': test}
#     return render(request, 'votes.html', context=context)