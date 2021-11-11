from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Customer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        error = []
        data= request.data

        username = data['username']
        if not username :
            error.append("Usuário é Necessário")
        first_name = data['first_name']
        if not first_name :
            error.append("Digite o Primeiro nome")
        last_name = data['last_name']
        if not last_name :
            error.append("Digite o Último nome")
        email = data['email']
        if not email :
            error.append("Email é necessário")
        password = make_password(data['password'])
        if not password :
            error.append("Senha é necessária")
        phone_number = data['phone_number']
        if not phone_number :
            error.append("Um telefone válido é requerido")

        if not error :
            try :
                cliente = Customer.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    phone_number=phone_number,
                )
                if cliente :
                    return Response({'success': True}, status=status.HTTP_201_CREATED)

            except Exception as e:
                cliente = Customer.objects.filter(email=email)
                if cliente :
                    cliente.delete()
                error.append("erro desconhecido")

        return JsonResponse({"success":False, 'errors':error}, status=status.HTTP_400_BAD_REQUEST)
        

class SignInView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):     

        if request.user.is_authenticated:
            return JsonResponse({"success":False, 'error': 'Você já esta autenticado'})
        username = request.data['username']  
        try :
            Customer.objects.get(username=username)
        except :
            return JsonResponse({"success":False, 'error':'Você tentou acessar com uma conta de painel, use o painel para isto'})
        password= request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            return JsonResponse({"success":True})
        else :
            return JsonResponse({"success":False, 'error':'Usuário e/ou senha inválidos'})
    '''
    TODO : Retorno para o template de cadastro caso usuario não esteja autenticado
    '''
    # return render(request, "")
         
def sign_out(request):    
    logout(request)
    return redirect('/auth/sign_up/')