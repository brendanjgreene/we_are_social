from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Magazine


@login_required(login_url='/login/')  # comment this out to use my alternative solution of disabling paypal form on magazine.html
def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})

