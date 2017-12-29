from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'upload/index.html', context)

@csrf_exempt
def file(request):
    print('ssss1' + request.method)
    if request.method == 'POST':  
        #print('ssss2' + request.POST.File)
        #print(request.POST.File)
        content = "request.POST.get('name1')"
        print(request.POST.items)
        print(request.POST.get('name1'))
        print(request.FILES)
        f = (request.FILES.get('file1'))
        print(request.POST.get('name1'))
        with open("files/" + request.POST.get('name1'), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        return HttpResponse('POST receive success, name is ' + content)  
    else:  
        content = "request.GET.get('name')"  
        return HttpResponse('GET receive success, name is ' + content)  
