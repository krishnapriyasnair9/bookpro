#create your views here
#add book
#list all book
#book detail
#edit book
#delete book

from django.shortcuts import render, redirect
from bookadd.forms import BookForm,OrderEditForm
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,TemplateView
from bookadd.models import Books
from customer.models import Orders
from django.core.mail import send_mail


class BookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "bookadd.html"
    success_url = reverse_lazy("allbooks")
    #def get(self,request):
        #form=BookForm()
        #return render(request,"bookadd.html",{"form":form})
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
class BookList(ListView):
    model = Books
    template_name = "book_list.html"
    context_object_name = "books"
    #def get(self,request):

        #qs=Books.objects.all()
        #return render(request,"book_list.html",{"books":qs})
class BookDetailView(DetailView):
    model = Books
    template_name = "book_details.html"
    context_object_name = "book"
    pk_url_kwarg = "id"
    #def get(self,request,*args,**kwargs):
        #qs=Books.objects.get(id=kwargs.get("id"))
        #return render(request,"book_details.html",{"book":qs})
class BookDelete(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")
class ChangeBook(UpdateView):
    model = Books
    template_name = "bookchange.html"
    form_class = BookForm
    success_url = reverse_lazy("changebook")
    pk_url_kwarg = "id"
    
    #def get(self,request,*args,**kwargs):
        #qs=Books.objects.get(id=kwargs.get("id"))
        #form=BookForm(instance=qs)
        #return render(request,"bookchange.html",{"form":form})
    def post(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        form=BookForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allbooks")
class DashBoardView(TemplateView):
    template_name = "dashboard.html"
    def get(self,request,*args,**kwargs):
        new_orders=Orders.objects.filter(status="orderplaced")
        return render(request,self.template_name,{"new_orders":new_orders})
class OrderDetailView(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "id"
class OrderChangeView(UpdateView):
    model = Orders
    template_name = "order_change.html"
    form_class = OrderEditForm
    pk_url_kwarg = "id"
    def get(self, request, *args, **kwargs):
        order=Orders.objects.get(id=kwargs["id"])
        return render(request,self.template_name,{"order":order,"form":self.form_class})
    def post(self, request, *args, **kwargs):
        order=Orders.objects.get(id=kwargs["id"])
        form=OrderEditForm(request.POST,instance=order)
        if form.is_valid():
            delivary_date=str(form.cleaned_data.get("expected_delivary_date"))
            form.save()
            send_mail(
                'Order Notification',
                'order will be delivered on'+delivary_date,
                'krishnapriyasnair9@gmail.com',
                ['krishnakitu0123@gmail.com'],
                fail_silently=False,
            )
            return redirect("dashboard")













