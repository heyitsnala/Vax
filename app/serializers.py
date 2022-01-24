from rest_framework import serializers
from vax.app.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email', 'address', 'postalCode', 'dateOfBirth', 'healthCardNum']
