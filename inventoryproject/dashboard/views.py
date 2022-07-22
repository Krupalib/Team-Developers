from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Recipes, userRecipes, Utensils,Ingredients,keywords,process_steps

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def recipe(request):
    return render(request, 'dashboard/Recipe.html')

def process(request):
    webpage_list = process_steps.objects.order_by('step_no')
    date_dict = {'access_records' : webpage_list}
