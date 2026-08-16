from django.shortcuts import render,redirect,get_object_or_404
from.models import URLMapping
from .utils import create_unique_token

# Create your views here.
def index(request):
    if request.method=='GET' :
        return render(request,"index.html")
    if request.method=='POST' :
        long_url = request.POST.get('long_url')
        short_token = create_unique_token(URLMapping)
        URLMapping.objects.create(long_url=long_url,short_token=short_token)
        return render(request, "index.html", {
            "new_url" : short_token
            })
    
    

def redirect_view(request,token):
    urlmapping = get_object_or_404(URLMapping,short_token=token)
    urlmapping.clicks+=1
    urlmapping.save()
    return redirect(urlmapping.long_url)