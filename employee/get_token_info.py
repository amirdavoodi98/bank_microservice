import jwt
from bank.models import Branch

def get_branchId_from_token(token):
    access_token = jwt.decode(token, options={"verify_signature": False})
    user_id = access_token['user_info']['user_id']
    branch = Branch.objects.get(manager_id=user_id)
    return branch.id

