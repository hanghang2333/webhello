from django.http import HttpResponse

s = []
for i in range(1000):
    if i%100==0:
        print(i)
    s.append(i)

def hello(request):
    return HttpResponse("Hello world")

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message ="Waht you search:"+request.GET['q']+str(s[100])
    else:
        message = "you give nothing"
    return HttpResponse(message)

