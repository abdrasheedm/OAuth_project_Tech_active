from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter


from .pagination import CustomPagination
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # permission_classes = [permissions.AllowAny,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_date']


class UserDetailsView(generics.RetrieveAPIView):
    # permission_classes = [permissions.AllowAny,]
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    












# class UserLoginView(APIView):
#     permission_classes = [permissions.AllowAny,]
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             print(user.username, '------------------------------------username--------------------------')
#             token = ''
#             time_threshold = datetime.now()
#             token_obj = AccessToken.objects.filter(user=user, expires__gt=time_threshold)
#             if token_obj:
#                 token_obj = token_obj[0]
#                 token = token_obj.token
#                 print(token, '------------------------------------token1--------------------------')

            
#             else:
#                 if not Application.objects.filter(user=user).exists():
#                     print('no application')
#                     Application.objects.create(user_id=user.id, authorization_grant_type='password', client_type='confidential')
#                 app_obj = Application.objects.filter(user=user)
#                 if app_obj:
#                     app_obj = app_obj[0]
#                     print(app_obj, '-----------------------app obj----------------------')
#                     client_id = app_obj.client_id
#                     client_secret = app_obj.client_secret
#                     print(client_id, client_secret, '=====================================')
#                     url = f"http://{request.get_host()}/o/token/"
#                     data_dict = {"grant_type":"password", "username":username, "password": password, "client_id" : client_id, "client_secret": client_secret}
#                     print(data_dict)
#                     response = requests.post(url, data=data_dict)
#                     if response.status_code == 200:

#                         data = json.loads(response.text)
#                         token = data.get("access_token")
#                         response = {
#                             "access_token": token
#                         }
#                     else:
#                         print(response.text)
            
#             print(token, 'access token ==================================')
#             return Response({"message": "login successfull"})
#         return Response({"message": "not authorized"})
    
