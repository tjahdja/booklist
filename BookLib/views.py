from django.shortcuts import render, redirect
from .forms import bookForm
from .models import BookEntry

# Create your views here.
def bookList(request):
    context = {'bookList': BookEntry.objects.all()}
    return render(request, "bookList.html", context)

def inputForm(request, id=0):
    if request.method == "GET":
        if id==0:
            form = bookForm()
        else:
            book = BookEntry.objects.get(pk=id)
            form = bookForm(instance=book)
        return render(request, "inputForm.html", {'form':form})
    else:
        if id==0:
            form = bookForm(request.POST)
        else:
            book = BookEntry.objects.get(pk=id)
            form = bookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return redirect('/list')

def bookDel(request,id):
    book = BookEntry.objects.get(pk=id)
    book.delete()
    return redirect('/list')