from django.shortcuts import render,redirect , HttpResponseRedirect 
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    prod = Product.objects.all()
    form = ProductForm(request.POST, request.FILES)  # Ensure request.FILES is included!

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")  # Redirect after adding a product

    return render(request, "clothing/home.html", {"prod": prod, "form": form})


def update_data(request, id):
    pi = Product.objects.get(pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=pi)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect after update
    else:
        form = ProductForm(instance=pi)

    return render(request, "clothing/update.html", {"form": form})


def delete_data(request, id):
    pi = Product.objects.get(pk=id)

    if request.method == "POST":
        pi.delete()
        return redirect("home")  # Redirect to home page after deletion

    return render(request, "clothing/confirm_delete.html", {"product": pi})  # Ask for confirmation before deletion