from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home (req):
    return render(req,'index.html')

#def home(req):
    #data={
       # 'name':"abhinav",
       # 'last':"saxena",
       # 'active':True,
       # 'active1':False,
   # }
   # return JsonResponse(data)
