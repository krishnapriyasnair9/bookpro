#create your views here
#add book
#list all book
#book detail
#edit book
#delete book

from django.shortcuts import render, redirect
from bookadd.forms import BookForm
from django.views.generic import View
from bookadd.models import Books


class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,"bookadd.html",{"form":form})
    def post(self,request):
        #n1=int(request.POST.get("num1"))
        #n2=int(request.POST.get("num2"))

        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            """n1=(form.cleaned_data.get("book_name"))
            n2=(form.cleaned_data.get("author"))
            n3 = (form.cleaned_data.get("price"))
            n4 = (form.cleaned_data.get("copies"))
            print(n1,"\n",n2,"\n",n3,"\n",n4)
            qs=Books(
                book_name=form.cleaned_data.get("book_name"),
                author=form.cleaned_data.get("author"),
                amount=form.cleaned_data.get("price"),
                copies=form.cleaned_data.get("copies")
            )
            qs.save()"""




            #result=int(n1)-int(n2)
            return render(request,"bookadd.html")
        else:
            return render(request,"bookadd.html",{"form":form})
class BookList(View):
    def get(self,request):
        qs=Books.objects.all()
        return render(request,"book_list.html",{"books":qs})
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        return render(request,"book_details.html",{"book":qs})
class BookDelete(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")
class ChangeBook(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        form=BookForm(instance=qs)
        return render(request,"bookchange.html",{"form":form})
    def post(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        form=BookForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allbooks")







