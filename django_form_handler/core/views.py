from django.shortcuts import render, redirect

from .models import FormData


def form_view(request):
    if request.method == "POST":
        data = []

        for key, value in request.POST.items():
            if key.startswith("name") and value:
                data.append(value)

        FormData.objects.create(data=data)

        return redirect("list")

    return render(request, "form.html")


def list_view(request):
    objects = FormData.objects.all()
    return render(request, "list.html", {"objects": objects})