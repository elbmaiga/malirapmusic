from django.shortcuts import render

def about(request):
    datas = {
        'title': 'about'
    }
    return render(request, 'about.html', datas)

def contact(request):
    datas = {
        'title': 'contatct'
    }
    return render(request, 'contact.html', datas)

def maintenance(request):
    datas = {
        'title': 'maintenance'
    }
    return render(request, 'maintenance.html', datas)