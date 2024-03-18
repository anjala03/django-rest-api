from rest_framework import serializers
from .models import People, Colors

class Colorserializer(serializers.ModelSerializer):
    class Meta:
        model=Colors
        # fields="__all__"
        fields=['id','color_name', 'color_code']

class PeopleSerializer(serializers.ModelSerializer):
    # just_color=Colorserializer(read_only=True)
    country=serializers.SerializerMethodField()
        #method to add extra field in the model, without having to manually create a field in model
    class Meta:
        model=People
        # fields="__all__"
        fields=["just_color","id", "name", "age", "sex", "country"]
               # depth=1 
        # fields=["name", "age"]
        #this is to include all the fields, if want to have specific you can do it as :  fields=["name", "age"], to exclude an: exclude=["sex"]

    def get_country(self,obj): 
        #the syntax is get_additional field name(self,obj)
        return "Nepal"

    def validate(self, data):
        for c in data["name"]:
            string= "@#$!~^&*)(|?"
            for s in string:   
                if s ==c:
                    print("invalid character found",s)
                    raise serializers.ValidationError({"message":" name cannot contain special characters"})
            try:
                if data.get('age'):
                    if(data["age"]>=18):
                        return data
            #  this  will  return a value which will be sent to the post method defned in the  view.py
                raise serializers.ValidationError({"message":"Age is less than 18"})
            except Exception as e:
                print("ageerror", e)
                return data
            
            
    


# normal kind of serializer, used in validation specifically, just the serializer class not the ModelSerializer, doesnot need the model, no data is savedd in the database, no use of create method
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=20)


    


        

