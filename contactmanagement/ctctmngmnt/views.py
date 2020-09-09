from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.decorators import api_view

@api_view(('GET',))
def contact_list(request, *args, **kwargs):
    queryset = Contact.objects.all()
    if queryset.exists():
        serialized_qs = ContactSerializer(queryset,many=True)
        return Response(serialized_qs.data,status=200)
    return Response({"msg":"error occured..."})    


@api_view(('GET',))
def contact_detail(request, pk, *args, **kwargs):
    qs = Contact.objects.filter(pk=pk)
    if qs.exists():
        serialized_qs = ContactSerializer(qs,many=True)
        return Response(serialized_qs.data,status=200)
    return Response({'msg':'not found...'},status=404)    

@api_view(('PUT','PATCH','GET'))
def contact_edit(request, pk, *args, **kwargs):
    object = Contact.objects.get(pk=pk)
    
    if request.method == "PUT":
        serializer = ContactSerializer(object,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=400) 
    serializer = ContactSerializer(object)        
    return Response(serializer.data,status=200)      
         



@api_view(('POST','GET'))
def new_contact(request, *args, **kwargs):
    if request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            print(serializer.errors)

    return Response({'msg':'error occurred...'})            


@api_view(('DELETE','GET'))
def delete_contact(request,pk, *args, **kwargs):
    qs = Contact.objects.get(pk=pk)
    if qs:
        serializer = ContactSerializer(qs)
        qs.delete()
        return Response(serializer.data,status=200)
    return Response({'msg':'error ocurred...'},status=404)



