from django.http import JsonResponse
from django.shortcuts import render

from bankingapp.models import Branch


# Create your views here.

def demo(request):
    return render(request, 'index.html')


def get_branches(request):
    if request.method == 'GET':
        district_id = request.GET.get('district_id')
        branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
        return JsonResponse(list(branches), safe=False)
