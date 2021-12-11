from django.shortcuts import render


def index(request):
    template_name = 'voos/index.html'
    context = {}
    render(request, template_name, context)
