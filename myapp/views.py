from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
import requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
def Register_form(request):
    
    return render(request,'register9.html')

def login_form(request):
    
    return render(request,'login9.html')
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

def dashboard_view(request):

    return render(request, 'dashboard/dashboard.html')
            
def dashboard_add_user(request):

    return render(request,'dashboard/add-user.html')

def dashboard_alert(request):

    return render(request,'dashboard/alert.html')  

def dashboard_assign_role(request):

    return render(request,'dashboard/assign-role.html')
  
def dashboard_avatar(request):

    return render(request,'dashboard/avatar.html')       

def dashboard_badges(request):

    return render(request,'dashboard/badges.html') 

def dashboard_button(request):

    return render(request,'dashboard/button.html')  

def dashboard_calendar_main(request):

    return render(request,'dashboard/calendar-main.html')  

def dashboard_calendar(request):

    return render(request,'dashboard/calendar.html')  

def dashboard_card(request):

    return render(request,'dashboard/card.html')  

def dashboard_carousel(request):

    return render(request,'dashboard/carousel.html')  

def dashboard_chat_empty(request):

    return render(request,'dashboard/chat-empty.html')  

def dashboard_chat_message(request):

    return render(request,'dashboard/chat-message.html')  

def dashboard_chat_profile(request):

    return render(request,'dashboard/chat-profile.html')  

def dashboard_code_generator_new(request):

    return render(request,'dashboard/code-generator-new.html')

def dashboard_code_generator(request):

    return render(request,'dashboard/code-generator.html') 

def dashboard_colors(request):

    return render(request,'dashboard/colors.html') 

def dashboard_column_chat(request):

    return render(request,'dashboard/column-chart.html')   

def dashboard_company(request):

    return render(request,'dashboard/company.html')   

def dashboard_currencies(request):

    return render(request,'dashboard/currencies.html')

def dashboard_developer_manager_approval(request):

    return render(request,'dashboard/developer-manager-approval.html')        

def dashboard_dropdown(request):

    return render(request,'dashboard/dropdown.html')  

def dashboard_email(request):

    return render(request,'dashboard/email.html') 

def dashboard_error(request):

    return render(request,'dashboard/error.html') 

def dashboard_faq(request):

    return render(request,'dashboard/faq.html') 

def dashboard_forgot_password(request):

    return render(request,'dashboard/forgot-password.html') 

def dashboard_form_layout(request):

    return render(request,'dashboard/form-layout.html') 

def dashboard_form_validation(request):

    return render(request,'dashboard/form-validation.html') 

def dashboard_form(request):

    return render(request,'dashboard/form.html') 

def dashboard_gallery(request):

    return render(request,'dashboard/gallery.html') 

def dashboard_image_generator(request):

    return render(request,'dashboard/image-generator.html') 

def dashboard_image_upload(request):

    return render(request,'dashboard/image-upload.html') 

def dashboard_index_2(request):

    return render(request,'dashboard/index-2.html') 

def dashboard_index_3(request):

    return render(request,'dashboard/index-3.html') 

def dashboard_index_4(request):

    return render(request,'dashboard/index-4.html') 


def dashboard_index_5(request):

    return render(request,'dashboard/index-5.html') 


def dashboard_index_6(request):

    return render(request,'dashboard/index-6.html') 


def dashboard_invoice_add(request):

    return render(request,'dashboard/invoice-add.html')

def dashboard_invoice_edit(request):

    return render(request,'dashboard/invoice-edit.html')

def dashboard_invoice_list(request):

    return render(request,'dashboard/invoice-list.html')   

def dashboard_invoice_preview(request):

    return render(request,'dashboard/invoice-preview.html') 

def dashboard_kanban(request):

    return render(request,'dashboard/kanban.html') 

def dashboard_language(request):

    return render(request,'dashboard/language.html') 

def dashboard_lead_managements(request):

    return render(request,'dashboard/lead-managements.html') 

def dashboard_lead_managements_data(request):

    return render(request,'dashboard/lead-managements-data.html') 

def dashboard_line_chart(request):

    return render(request,'dashboard/line-chart.html') 

def dashboard_list(request):

    return render(request,'dashboard/list.html') 

def dashboard_marketplace_details(request):

    return render(request,'dashboard/marketplace-details.html') 

def dashboard_marketplace(request):

    return render(request,'dashboard/marketplace.html') 

def dashboard_notification_alert(request):

    return render(request,'dashboard/notification-alert.html') 

def dashboard_notification(request):

    return render(request,'dashboard/notification.html') 

def dashboard_manager_approval(request):

    return render(request,'dashboard/manager-approval.html') 

def dashboard_pagination(request):

    return render(request,'dashboard/pagination.html') 

def dashboard_payment_gateway(request):

    return render(request,'dashboard/payment-gateway.html') 

def dashboard_pie_chart(request):

    return render(request,'dashboard/pie-chart.html') 

def dashboard_portfolio(request):

    return render(request,'dashboard/portfolio.html') 

def dashboard_pricing(request):

    return render(request,'dashboard/pricing.html') 

def dashboard_progress(request):

    return render(request,'dashboard/progress.html') 

def dashboard_radio(request):

    return render(request,'dashboard/radio.html') 

def dashboard_role_access(request):

    return render(request,'dashboard/role-access.html') 

def dashboard_sign_in(request):

    return render(request,'dashboard/sign-in.html') 

def dashboard_sign_up(request):

    return render(request,'dashboard/sign-up.html')

def dashboard_star_rating(request):

    return render(request,'dashboard/star-rating.html')  

def dashboard_starred(request):

    return render(request,'dashboard/starred.html') 

def dashboard_switch(request):

    return render(request,'dashboard/switch.html') 

def dashboard_table_basic(request):

    return render(request,'dashboard/table-basic.html')

def dashboard_table_data(request):

    return render(request,'dashboard/table-data.html') 

def dashboard_tabs(request):

    return render(request,'dashboard/tabs.html')  

def dashboard_tags(request):

    return render(request,'dashboard/tags.html')

def dashboard_terms_condition(request):

    return render(request,'dashboard/terms-condition.html') 

def dashboard_text_generator_new(request):

    return render(request,'dashboard/text-generator-new.html')  

def dashboard_text_generator(request):

    return render(request,'dashboard/text-generator.html') 

def dashboard_theme(request):

    return render(request,'dashboard/theme.html')  

def dashboard_tooltip(request):

    return render(request,'dashboard/tooltip.html') 

def dashboard_typography(request):

    return render(request,'dashboard/typography.html')

def dashboard_users_grid(request):

    return render(request,'dashboard/users-grid.html')

def dashboard_users_list(request):

    return render(request,'dashboard/users-list.html')


def dashboard_view_details(request):

    return render(request,'dashboard/view-details.html')

def dashboard_video_generator(request):

    return render(request,'dashboard/video-generator.html')

def dashboard_videos(request):

    return render(request,'dashboard/videos.html')

def dashboard_view_profile(request):

    return render(request,'dashboard/view-profile.html')

def dashboard_voice_generator(request):

    return render(request,'dashboard/voice-generator.html')

def dashboard_wallet(request):

    return render(request,'dashboard/wallet.html')

def dashboard_widgets(request):

    return render(request,'dashboard/widgets.html')

def dashboard_wizard(request):

    return render(request,'dashboard/wizard.html')

def dashboard_raise_request(request):
    
    return render(request,'dashboard/raise-request.html')





       
           


from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer ,RaiseRequestSerializer, main_tr_nd_histrySerializer, UpdateManagerapprovalSerializer, ManagerapprovalSerializer,DeveloperApprovalSerializer, LeadManagementsSerializer, LeadManagementsDataSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Raise_Request_Documentation, lead_managements
from django.db.models import Q
from datetime import datetime
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # Handle file uploads by combining request.data and request.FILES
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if 'uploadimage' in request.FILES:
            serializer.initial_data['profile_image'] = request.FILES.get('uploadimage')
        if 'uploadpan' in request.FILES:
            serializer.initial_data['pan_card_image'] = request.FILES.get('uploadpan')
        if 'uploadaadharcard' in request.FILES:
            serializer.initial_data['aadhar_card_image'] = request.FILES.get('uploadaadharcard')
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': RegisterSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Extract user from validated data
            user = serializer.validated_data['user']
            
            # Create JWT tokens
            refresh = RefreshToken.for_user(user)
            
            # Create response object
            response = Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            
            # Set tokens in cookies
            response.set_cookie('access', str(refresh.access_token), httponly=True, samesite='Strict')
            response.set_cookie('refresh', str(refresh), httponly=True, samesite='Strict')
            
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Requestview(generics.GenericAPIView):
    
     serializer_class = RaiseRequestSerializer   
     
     def post(self, request, *args, **kwargs):
        # Handle file uploads by combining request.data and request.FILES
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if 'attachments' in request.FILES:
            serializer.initial_data['attach_file_original'] = request.FILES.get('attachments')
       
        
        if serializer.is_valid():
            request = serializer.save()
           
            return Response({
                'request': RaiseRequestSerializer(request).data,
               
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     def get(self, request, *args, **kwargs):
        records = Raise_Request_Documentation.objects.all()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)
    
    
class Historyview(generics.GenericAPIView):
    
     serializer_class = main_tr_nd_histrySerializer   
     
     def post(self, request, *args, **kwargs):
        # Handle file uploads by combining request.data and request.FILES
        serializer = self.get_serializer(data=request.data, context={'request': request})
    
        if serializer.is_valid():
            request = serializer.save()
           
            return Response({
                'request': main_tr_nd_histrySerializer(request).data,
               
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class Managerapprovalview(generics.GenericAPIView):
     
     serializer_class = ManagerapprovalSerializer  
     
     def get(self, request, *args, **kwargs):
        records = Raise_Request_Documentation.objects.all()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)   


class Updatemanagerapprovalview(generics.GenericAPIView):
     
     serializer_class = UpdateManagerapprovalSerializer  
     records = Raise_Request_Documentation.objects.all()
     
     
     
     def put(self, request, *args, **kwargs):
            id= request.data.get('id')
            approval_type= request.data.get('approval_type')
            print("approval_type",approval_type)
            
            if not id:
                    return Response({"error": "id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
            if not Raise_Request_Documentation.objects.filter(id=id).exists():
                return Response({"error": f"requester with id '{id}' not found"}, status=status.HTTP_404_NOT_FOUND)

            
            requester = Raise_Request_Documentation.objects.get(id=id)
            
            
            print("rqstnr",requester)
           
                

            # Deserialize and validate the incoming data (partial=True allows partial updates)
            serializer = self.get_serializer(requester, data=request.data, partial=True)
            
            if serializer.is_valid():
                # Save the updated data (only the fields passed will be updated)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class DeveloperApprovalView(generics.GenericAPIView):
     
     serializer_class = DeveloperApprovalSerializer  
     
     def get(self, request, *args, **kwargs):
        records = Raise_Request_Documentation.objects.all()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)     
    
     
    
class LeadManagementsView(generics.GenericAPIView):
    
    serializer_class = LeadManagementsSerializer   
     
    def post(self, request, *args, **kwargs):
        # Handle file uploads by combining request.data and request.FILES
        serializer = self.get_serializer(data=request.data, context={'request': request})
    
        if serializer.is_valid():
            request = serializer.save()
           
            return Response({
                'request': LeadManagementsSerializer(request).data,
               
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    
    
class LeadManagementsData(generics.GenericAPIView):
     
     serializer_class = LeadManagementsDataSerializer  
     
     def get(self, request, *args, **kwargs):
        records = lead_managements.objects.all()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)  
    
    
     def post(self, request, *args, **kwargs):
      
         emp_code = request.data.get('emp_code')
         timestamp = request.data.get('timestamp')
         
         
         if not emp_code:
             return Response({'detail': 'Employee code not provided'}, status=status.HTTP_400_BAD_REQUEST)

         query =Q(emp_code=emp_code)
         
         if timestamp:
             try:
            # Parse timestamp to a date object
                timestamp_date = datetime.strptime(timestamp, '%Y-%m-%d').date()
            # Add date filter to the query
                query &= Q(timestamp__date=timestamp_date)
                
             except ValueError:
                
                  return Response({'detail': 'Invalid timestamp format'}, status=status.HTTP_400_BAD_REQUEST)
        
        
         filtered_data = lead_managements.objects.filter(query)
         serializer = self.get_serializer(filtered_data, many=True)
         return Response(serializer.data)
    
    
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"detail": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
            return Response({"detail": "Refresh token is missing"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDataSerializer


class UserDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("False")
            return redirect('/')  # Redirect to the home page if not authenticated
        print("TRUE")
        serializer = UserDataSerializer(request.user)
        return Response(serializer.data)