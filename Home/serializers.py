from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=People
        fields="__all__"
        # fields=["name", "age"]
        #this is to include all the fields, if want to have specific you can do it as :  fields=["name", "age"], to exclude an: exclude=["sex"]

        def validate(self, data):
            print(data)
            if data["age"]<=18:
                raise serializers.ValidationError({"message":"Age is less than 18"})
            print("hiiii")
            return data


        

