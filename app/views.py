from django.shortcuts import render

# Create your views here.
def filters_inbuilt(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HAi hoW aRe YoU','dt':dt,'c':12}
    return render(request,'filters_inbuilt.html',d)
