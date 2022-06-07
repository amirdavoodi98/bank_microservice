import jwt
from employee.models import Employee

def get_branchId_from_token(token):
    access_token = jwt.decode(token, options={"verify_signature": False})
    user_id = access_token['user_info']['user_id']
    employee = Employee.objects.get(employee_id=user_id)
    return employee.branch.id

