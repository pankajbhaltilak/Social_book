from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Books

# Create your views here.
def uploadfile(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        description = request.POST['description']
        visibility = request.POST.get('visibility') == 'on'
        Year_of_published = request.POST['Year_of_published']
        Cost = request.POST['Cost']
        files = request.FILES["file"]
        new_book = Books(file=files, file_name=file_name, description=description, visibility=visibility, Year_of_published=Year_of_published, Cost=Cost)
        new_book.save()
        messages.success(request, 'Your file is successfully uploaded!')
        return render(request, 'uploadfile.html')
    elif request.method == 'GET':
        return render(request, 'uploadfile.html')
    return render(request, 'uploadfile.html')

def bookdashboard(request):
    if 'data' in request.GET:
        data = request.GET['data']
        book = Books.objects.filter(file_name__icontains=data)
    
    else:
        book = Books.objects.all()
    context = {
        'Books': book
    }
    print(context)
    return render(request, 'bookdashboard.html', context)

def deleteBook(request, id):
    item = Books.objects.get(id=id)
    item.delete()
    messages.success(request, 'Your file is Deleted')
    return render(request, 'bookdashboard.html')
