from django.shortcuts import render
from .models import College

def home(request):
    colleges = College.objects.all()

    q = request.GET.get('q')
    if q:
        colleges = colleges.filter(name__icontains=q)

    return render(request,'home.html',{'colleges':colleges})

def college_detail(request, id):
    college = College.objects.get(id=id)
    return render(request, 'detail.html', {'college': college})
def landing(request):
    return render(request, 'landing.html')
from django.http import JsonResponse

def ai_chat(request):
    query = request.GET.get('q','').lower()

    colleges = College.objects.all()
    response = "I couldn't find anything."

    if "iit" in query:
        data = colleges.filter(name__icontains="IIT")
        response = ", ".join([c.name for c in data])

    elif "nit" in query:
        data = colleges.filter(name__icontains="NIT")
        response = ", ".join([c.name for c in data])

    return JsonResponse({"reply": response})
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import College, Favourite

@login_required
def add_fav(request, id):
    college = College.objects.get(id=id)
    Favourite.objects.create(user=request.user, college=college)
    return redirect('/home/')
from django.shortcuts import render, get_object_or_404
from .models import College

def college_detail(request, id):
    college = get_object_or_404(College, id=id)
    return render(request, 'college_detail.html', {'college': college})
def landing(request):
    return render(request,'landing.html')
from django.http import JsonResponse
from .models import College
def ai_chat(request):
    query = request.GET.get('q','').lower()

    colleges = College.objects.all()

    results = []

    for c in colleges:
        text = f"{c.name} {c.courses} {c.clubs} {c.labs} {c.placements}".lower()

        if query in text:
            results.append({
                "name": c.name,
                "location": c.location,
                "fees": c.fees,
                "avg": c.average_package
            })

    if results:
        return JsonResponse({"data": results[:3]})

    return JsonResponse({"data": "I couldn't find anything."})


