from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# if request.method == 'POST':
		# return HttpResponse(request.POST['item_text'])
	# if request.method == 'POST':
		# Item.objects.create(text=request.POST['item_text'])
		# return redirect('/lists/the-only-list-in-the-world/')
	return render(request,'home.html')
	
def view_list(request,list_id):
	list_ = List.objects.get(id=list_id)
	error=None
	
	if request.method=='POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect('/lists/%d/' % (list_.id,))
		except ValidationError:
			error = "You can't have an empty list item"
			
	return render(request,'list.html',{'list': list_, 'error': error})
	
def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error="You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))
	