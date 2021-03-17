from django.shortcuts import render

# Create your views here.
def setcookie(request):
    reponse = render(request,'student/setcookie.html')
    reponse.set_cookie('name','firoz')
    return reponse

def getcookie(request):
    name=request.COOKIES['name']
    return render(request,'student/getcookie.html',{'name':name})


del cookie(request):

