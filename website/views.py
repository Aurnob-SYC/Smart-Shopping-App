from django.shortcuts import render
from django.http import JsonResponse
from product_list_smart_suggestion.models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')  

def search_suggestions(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = list(Product.objects.filter(name__icontains=query).values('name')[:5])  # limit 5
    else:
        results = []
    return JsonResponse(results, safe=False)