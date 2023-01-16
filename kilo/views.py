from django.shortcuts import render, redirect
from django.utils import timezone
from PIL import Image

from . import models
from . import forms


def home(request):
    if request.method == "POST":
        form = forms.FaylForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            choice = form.cleaned_data.get("file_field")
            if choice == 'png':
                return redirect('png', file_id=form.instance.id)
            elif choice == 'jpg':
                return redirect('jpg', file_id=form.instance.id)
    else:
        form = forms.FaylForm()
    return render(request, 'kilo/home.html', {'form': form})


def make_jpg(request, file_id):
    fayl = models.File.objects.get(id=file_id)
    time = timezone.now().strftime("%Y-%m-%d")
    img = Image.open(fayl.document)
    jpg = img.convert('RGB')
    path = f'media/temp/geek-{time}.jpg'
    jpg.save(path)
    jpg_converted = models.FileUser.objects.create(documentUser=path)
    return render(request, 'kilo/jpg.html', {'jpg_converted': jpg_converted})


def make_png(request, file_id):
    fayl = models.File.objects.get(id=file_id)
    time = timezone.now().strftime("%Y-%m-%d")
    img = Image.open(fayl.document)
    png = img.convert('RGB')
    path = f'media/temp/geek-{time}.png'
    png.save(path)
    png_converted = models.FileUser.objects.create(documentUser=path)
    return render(request, 'kilo/png.html', {'png_converted': png_converted})
