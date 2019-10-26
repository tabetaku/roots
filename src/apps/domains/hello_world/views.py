from django.shortcuts import render
from django.views import View


class HelloWorldView(View):
    @staticmethod
    def get(request):
        return render(request, 'hello_world/index.html', {})
