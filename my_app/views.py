from django.shortcuts import render
from .models import Todo
from django.utils import timezone 
#from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
	todo_items = Todo.objects.all().order_by("-added_date")
	#print(todo_items)
	return render (request, "base.html", {"todo_items" : todo_items}) 

#@csrf_exempt
@csrf_protect
def add_todo(request):
	current_date = timezone.now()
	#print (current_date)
	content = request.POST["content"]
	#print(content)
	created_obj = Todo.objects.create(added_date= current_date, text=content)
	length_of_todos = Todo.objects.all().count()
	return HttpResponseRedirect("/")

@csrf_protect
def delete_todo(request, todo_id):
	Todo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect("/")

