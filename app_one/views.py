from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    print(request.POST)
    name_form = request.POST['name']
    location_form = request.POST['location']
    language_form = request.POST['language']
    comment_form = request.POST['comment']
    context = {
        'name_form':name_form,
        'location_form':location_form,
        'language_form':language_form,
        'comment_form':comment_form
    }
    return render(request, 'result.html', context)
