from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import tv
# Create your views here.

def registertv(request):
    return render(request,'RegisterTv.html')

def viewdetails(request):
    modelnoo=request.POST['modelno']
    namee=request.POST['name']
    typee=request.POST['type']
    featuress=request.POST.getlist('feature')

    colorr=request.POST['color']
    pricee=request.POST['price']
    check = tv.objects.filter(model_no=modelnoo)
    if check:
        return HttpResponse("Item Already Exists")
    else:
        data = tv(model_no=modelnoo,tv_name=namee,type=typee,color=colorr,price=pricee,features=featuress)
        data.save()

    data1 = tv.objects.all()
    return render(request,'ViewDetails.html',{'r':data1})


def display(request):
    data1 = tv.objects.all()
    return render(request, 'ViewDetails.html', {'r': data1})


def addstock(request):
    a = request.POST['modelnum']
    return render(request,'AddStock.html',{'data':a})

def stock_rack_add(request):
    a = request.POST['modelnum']
    rackno = request.POST['rack']
    stockno = request.POST['stock']
    tv.objects.filter(model_no=a).update(rack=rackno,stock=stockno)
    return redirect(display)

