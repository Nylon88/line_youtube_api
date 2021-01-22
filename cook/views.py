from django.shortcuts import render, HttpResponse


def temp_response(request):
    # return HttpResponse('Hello')
    return render(request, 'cook/temp_html/temp.html')