from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework import generics

from Test1.models import *
from Test1.serializers import *
from django.http import Http404


# Create your views here.
# @csrf_exempt
# def DiseaseTypeApi(request, id = 0):
#     if request.method=='GET':
#         diseasetypes = DiseaseType.objects.all()
#         diseasetype_serializer = DiseaseTypeSerializer(diseasetypes, many = True)
#         return JsonResponse(diseasetype_serializer.data, safe= False)
#     elif request.method=='POST':
#         diseasetypes_data = JSONParser().parse(request)
#         diseasetype_serializer=DiseaseTypeSerializer(data=diseasetypes_data)
#         if diseasetype_serializer.is_valid():
#             diseasetype_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method=='PUT':
#         diseasetypes_data = JSONParser().parse(request)
#         diseasetype = DiseaseType.objects.get(diseasetypeID = diseasetypes_data['diseaseID'])
#         diseasetype_serializer = DiseaseTypeSerializer(diseasetype, data=diseasetypes_data)
#         if diseasetype_serializer.is_valid():
#             diseasetype_serializer.save()
#             return JsonResponse("Update Successfully", safe= False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         diseasetype = DiseaseType.objects.get(diseaseID = id)
#         diseasetype.delete()
#         return JsonResponse("Deleted Successfully", safe=False)


# @csrf_exempt
# def CountryApi(request, countryname = 0):
#     if request.method=='GET':
#         countrynames = Country.objects.all()
#         countryname_serializer = CountrySerializer(countrynames, many = True)
#         return JsonResponse(countryname_serializer.data, safe= False)
#     elif request.method=='POST':
#         countrynames_data = JSONParser().parse(request)
#         countryname_serializer=CountrySerializer(data=countrynames_data)
#         if countryname_serializer.is_valid():
#             countryname_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method=='PUT':
#         countrynames_data = JSONParser().parse(request)
#         countryname = Country.objects.get(cname = countrynames_data['cname'])
#         countryname_serializer = CountrySerializer(countryname, data=countrynames_data)
#         if countryname_serializer.is_valid():
#             countryname_serializer.save()
#             return JsonResponse("Update Successfully", safe= False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         countryname = Country.objects.get(cname = countryname)
#         countryname.delete()
#         return JsonResponse("Deleted Successfully", safe=False)


def homepage(request):
    return render(request, 'index.html')

# class DiseaseType(APIView):
#     def get(self, request, format = None):
#         diseasetypes = DiseaseType.objects.all()
#         diseasetype_serializer = DiseaseTypeSerializer(diseasetypes, many = True)
#         return JsonResponse(diseasetype_serializer.data)
#     def post(self, request, format=None):
#         diseasetype_serializer = DiseaseTypeSerializer(data=request.data)
#         if diseasetype_serializer.is_valid():
#             diseasetype_serializer.save()
#             return JsonResponse(diseasetype_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(diseasetype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DiseaseTypeList(generics.ListCreateAPIView):
    queryset = DiseaseType.objects.all()
    serializer_class = DiseaseTypeSerializer

class DiseaseTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiseaseType.objects.all()
    serializer_class = DiseaseTypeSerializer


class CountryListApi(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    def put(self, request, pk, format=None):
        print(request.data)
        try:
            doctor = Country.objects.get(cname = pk)
        except Country.DoesNotExist:
            raise Http404('Not found')
        serializer = CountrySerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiseaseList(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DiscoverList(generics.ListCreateAPIView):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer
    def post(self, request, format=None):
        serializer = DiscoverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscoverDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class PublicServantList(generics.ListCreateAPIView):
    queryset = PublicServant.objects.all()
    serializer_class = PublicServantSerializer

class PublicServantDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class SpecializeList(generics.ListCreateAPIView):
    queryset = Specialize.objects.all()
    serializer_class = SpecializeSerializer
    def post(self, request, format=None):
        serializer = SpecializeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecializeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialize.objects.all()
    serializer_class = SpecializeSerializer

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer