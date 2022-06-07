from rest_framework.viewsets import ModelViewSet
from account.models import Account
import grpc
from rest_framework.response import Response
from rest_framework import status

from account.serializers import CreateAccountSerializer, CreateUserAcountSerializer
from .permissions import IsEmployee
from grpc_auth import user_pb2, user_pb2_grpc
from .get_info_from_token import get_branchId_from_token

class CreateAccountViewSet(ModelViewSet):
    serializer_class = CreateUserAcountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsEmployee]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = user_pb2_grpc.UserControllerStub(channel)
            response = stub.Create(user_pb2.User(username=serializer.validated_data['username'],
                                                            password=serializer.validated_data['password'],
                                                            user_type='Customer',
                                                            mobile_number=serializer.validated_data['mobile_number']))

        branch_id = get_branchId_from_token(str(request.headers.get('Authorization')).split(' ')[1])
        customer_id = response.id
        data = {'customer_id': customer_id, 'branch_id': branch_id, 'balance': serializer.validated_data['balance']}
        account_serializer = CreateAccountSerializer(data=data)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()

        return Response(account_serializer.data, status=status.HTTP_201_CREATED)
