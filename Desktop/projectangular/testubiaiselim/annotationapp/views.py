from .models import Annotation
from .serializers import AnnotationSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



# Create your views here.
@csrf_exempt
def annotationApi(request,id=0):
    if request.method=='GET':
        annotations = Annotation.objects.all()
        serializer_get = AnnotationSerializer(annotations, many=True)
        return JsonResponse(serializer_get.data, safe= False)

    elif request.method=='POST':
        annotations= JSONParser().parse(request)
        serializer_post = AnnotationSerializer(data=annotations)
        if serializer_post.is_valid():
            serializer_post.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
