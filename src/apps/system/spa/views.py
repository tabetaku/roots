from django.shortcuts import render
from django.views import View


class SpaView(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html', {})
