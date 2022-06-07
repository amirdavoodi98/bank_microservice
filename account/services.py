import jwt
from django_grpc_framework import generics

from protos import card_to_card_pb2
from .serializers import CardToCardProtoSerializer
from .permissions import IsCustomer
from .models import Account

class CardToCardService(generics.ModelService):
    serializer_class = CardToCardProtoSerializer
    permission_class = [IsCustomer]
    def CardToCard(self, request, context):
        response = card_to_card_pb2.CardToCardResponse()

        metadata = dict(context.invocation_metadata())
        user_token = str(metadata['access_token'])
        access_token = jwt.decode(user_token, options={"verify_signature": False})
        userID = access_token['user_info']['user_id']

        src_account = Account.objects.get(customer_id=userID)
        dest_account = Account.objects.get(account_no=request.dest_account_no)
        amount = request.amount

        if src_account.balance < amount:
            response.resp = "not enuagh balance"
            response.status = 401
            return response

        src_account.balance = src_account.balance - amount
        src_account.save()
        dest_account.balance = dest_account.balance+ amount
        dest_account.save()
        
        response.resp = "succesfully"
        response.status = 200

        return response