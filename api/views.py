from django.http import JsonResponse


def hello(request,*args,**kwargs) :
  return JsonResponse({"message":"Hello World"})
