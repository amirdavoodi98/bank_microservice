from rest_framework.viewsets import ModelViewSet
import grpc
from rest_framework.response import Response
from rest_framework import status

from employee.models import Employee
from employee.permissions import IsBranchManager
from employee.serializers import CreateEmployeeSerializer, UserSerializer
from grpc_auth import user_pb2, user_pb2_grpc
from .get_token_info import get_branchId_from_token

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer
    permission_classes = [IsBranchManager]

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = user_pb2_grpc.UserControllerStub(channel)
            response = stub.Create(user_pb2.User(username=user_serializer.validated_data['username'],
                                                             password=user_serializer.validated_data['password'],
                                                             user_type='Employee',
                                                              mobile_number=user_serializer.validated_data['mobile_number']))
        print(response)
        branch_id = get_branchId_from_token(str(request.headers.get('Authorization')).split(' ')[1])
        print(branch_id)
        data = {'employee_id': response.id, 'branch_id': branch_id}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = self.perform_create(serializer)

        return Response(response, status=status.HTTP_201_CREATED)
