from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

def message(request):
    return HttpResponse('OK')


# line hookを受け取る。
class LineHook(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('このサイトは利用できません')

    def post(self, request):
        return HttpResponse('ok')
