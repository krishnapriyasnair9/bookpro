from django import forms
from bookadd.models import Books
from customer.models import Orders
"""class BookForm(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        copies = cleaned_data.get("copies")
        if price < 0:
            msg = "please provide a valid number"
            self.add_error("price", msg)
        if copies < 0:
            msg = "please provide a valid number"
            self.add_error("copies", msg)"""
class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),

        }
class OrderEditForm(forms.ModelForm):
    options = (
        ("orderplaced", "orderplaced"),
        ("dispatched", "dispatched"),
        ("in_transit", "in_transit"),
        ("delivered", "delivered")


    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"from-select"}))
    class Meta:
        model=Orders
        fields=["expected_delivary_date","status"]
        widgets={
            "expected_delivary_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "status":forms.Select(attrs={"class":"form-select"})
        }


