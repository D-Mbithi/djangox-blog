from django.shortcuts import render

# Create your views here.


def profile(request):
    """User profile"""

    template = "accounts/profile.html"
    context = {}

    return render(request, template, context)
