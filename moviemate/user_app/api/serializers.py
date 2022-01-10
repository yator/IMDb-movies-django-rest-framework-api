from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers

class RegistrationSerializers(serializers.ModelSerializer):

    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields =['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):

       password = self.validated_data['password']
       password2 = self.validated_data['password2']
    
       if password !=password2:
          raise serializers.ValidationError({'error':'password1 and password2 does not match!'})
    
       if User.objects.filter(email=self.validated_data['email']).exists():
           raise serializers.ValidationError({'error':'Email already Exists!'})

       account=User(email=self.validated_data['email'],username=self.validated_data['username'])
       account.set_password(password)
       account.save()

       return account    