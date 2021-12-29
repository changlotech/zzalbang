from django.shortcuts import render



def notice(request):
    return render(request, 'infoapp/notice.html')

def info(request):
    return render(request, 'infoapp/info.html')

def contact(request):
    return render(request, 'infoapp/contact.html')

def company(request):
    return render(request, 'infoapp/company.html')