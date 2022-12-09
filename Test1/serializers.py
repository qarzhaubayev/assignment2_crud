from rest_framework import serializers
from Test1.models import *
from rest_framework import viewsets

class DiseaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseType
        fields = ('diseaseID', 'diseaseDescription')

# class Step2ViewSet(viewsets.ModelViewSet):
#     serializer_class = DiseaseTypeSerializer

#     def get_queryset(self):
#         return DiseaseType.objects.filter(pk=self.request.user.profile.id)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('cname', 'population')


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('disease_code', 'pathogen','description','diseaseID')


class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discover
        fields = ('cname', 'disease_code','first_enc_date')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'name','surname','salary', 'phone' , 'cname')
class PublicServantSerializer(serializers.ModelSerializer):#
    class Meta:
        model = PublicServant
        fields = ('email', 'department')
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('email', 'degree')
class SpecializeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('diseaseID', 'email')
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('cname', 'email','disease_code','total_deaths', 'total_patients')