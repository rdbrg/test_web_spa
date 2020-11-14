from django.shortcuts import render, redirect
# from django.http import HttpResponse
#
# from .models import *
from .forms import *


def index(request):
    data = Data.objects.all()

    form = PassForm()

    if request.method == 'POST':
        form = PassForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'passhold': data, 'form': form}
    return render(request, 'passhold/index.html', context)


def update_data(request, pk):
    data = Data.objects.get(id=pk)

    form = PassForm(instance=data)

    if request.method == 'POST':
        form = PassForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'passhold/update_data.html', context)


def delete_data(request, pk):
    item = Data.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'passhold/delete_data.html', context)
