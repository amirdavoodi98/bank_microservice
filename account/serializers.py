from rest_framework import serializers
from django_grpc_framework import proto_serializers
import random

from .models import Account

def generate_account_no():
    account_no = str(random.randint(100000000, 999999999))
    return account_no

class CreateUserAcountSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=11)
    balance = serializers.IntegerField(default=0)

class CreateAccountSerializer(serializers.ModelSerializer):
    account_no = serializers.CharField(max_length=10, required=False)
    branch_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Account
        fields = ('account_no', 'branch_id', 'balance', 'customer_id')
    
    def create(self, validated_data):
        validated_data['account_no'] = generate_account_no()
        return super().create(validated_data)

class CardToCardProtoSerializer(proto_serializers.ProtoSerializer):
    dest_account_no = serializers.CharField(max_length=10)
    amount = serializers.IntegerField()