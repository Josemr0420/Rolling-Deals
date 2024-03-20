from django.shortcuts import render, redirect
from .models import Rating
from .forms import RatingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

@login_required
def create_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            user = request.user
            rating = form.save(commit=False)
            rating.user = user
            rating.save()
            return redirect('home')
    else:
        form = RatingForm()
    return render(request, 'rating/create_rating.html', {'form' : form}) 
