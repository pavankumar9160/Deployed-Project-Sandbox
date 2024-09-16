from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import random
import string
from .models import Raise_Request_Documentation, main_tr_nd_histry,lead_managements


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    profile_image = serializers.ImageField(required=False)
    pan_card_image = serializers.ImageField(required=False)
    aadhar_card_image = serializers.ImageField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'dob', 'gndr', 'blood_group', 'marital_status', 'marriage_date',
            'current_address', 'phno', 'qualification', 'rolename', 'pan', 'aadhar_number', 'bank_acc',
            'bank_name', 'bank_ifsc', 'bank_holder_name', 'ip_address', 'mail_id', 'password', 'password2',
            'profile_image', 'pan_card_image', 'aadhar_card_image'
        )

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 as it's not required

        def generate_unique_empcode(first_name, last_name):
            # Ensure that first_name and last_name are provided, otherwise use placeholders
            first_name = first_name or "FN"
            last_name = last_name or "LN"
            
            # Concatenate first_name and last_name and make it uppercase
            empcode = (first_name + last_name).upper()
            
            # Retry to find a unique empcode
            for _ in range(10):  # Retry up to 10 times
                if not User.objects.filter(empcode=empcode).exists():
                    return empcode
                empcode = (first_name + last_name).upper()  # Add random digits if necessary
            raise RuntimeError("Failed to generate a unique employee code. Please try again.")

        # Get first_name and last_name from validated data
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')

        # Generate unique employee code
        random_empcode = generate_unique_empcode(first_name, last_name)

        # Create user instance with empcode
        user = User(**validated_data)
        user.empcode = random_empcode
        user.set_password(validated_data['password'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    mail_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return {'user': user}

# serializers.py

from rest_framework import serializers


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'mail_id']  # Add any other fields you need


class RaiseRequestSerializer(serializers.ModelSerializer):
    
    rqstnr = serializers.CharField(required=False)
    approve_by = serializers.CharField(required=False)
    module = serializers.IntegerField(required=False)
    reqt_type = serializers.IntegerField(required=False)
    rqstd_date = serializers.DateField(required=False)
    desc = serializers.CharField(required=False)
    attach_file_original = serializers.ImageField(required=False)
    
    
    class Meta:
        model = Raise_Request_Documentation 
        fields = ['rqstnr', 'approve_by','module','reqt_type','rqstd_date','desc','attach_file_original']
        
    def create(self, validated_data):
    
        request_data = Raise_Request_Documentation.objects.create(
             rqstnr=validated_data.get('rqstnr'),
            approve_by=validated_data.get('approve_by'),
            module=validated_data.get('module'),
            reqt_type=validated_data.get('reqt_type'),
            rqstd_date=validated_data.get('rqstd_date'),
            desc=validated_data.get('desc'),
            attach_file_original=validated_data.get('attach_file_original')
        )
        return request_data    
    
    

class main_tr_nd_histrySerializer(serializers.ModelSerializer):
    
    main_tr_slno = serializers.IntegerField(required=False)
    resp = serializers.IntegerField(required=False)
    user = serializers.CharField(required=False)
    remarks = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    createdby = serializers.CharField(required=False)
    delete1 = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    timestamp = serializers.DateTimeField(required=False)
    
    
   
    class Meta:
        model = main_tr_nd_histry  
        fields = ['main_tr_slno','resp','user','remarks','date','createdby','delete1','status','timestamp']
        
    def create(self, validated_data):
    
        request_data = main_tr_nd_histry.objects.create(
             user=validated_data.get('user'),
            date=validated_data.get('date'),
            createdby = validated_data.get('createdby'),
            timestamp = validated_data.get('timestamp'),
            main_tr_slno=validated_data.get('main_tr_slno'),
            resp=validated_data.get('resp'),
            remarks=validated_data.get('remarks'),
            delete1=validated_data.get('delete1'),
            status=validated_data.get('status'),
            
        )
        return request_data         
    
class ManagerapprovalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Raise_Request_Documentation 
        fields = ['id','rqstnr', 'approve_by','module','reqt_type','rqstd_date','desc','attach_file_original','rmrks','approve_sts']
        
        
class UpdateManagerapprovalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Raise_Request_Documentation 
        fields = ['id','approve_sts','rmrks']     
        

class DeveloperApprovalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Raise_Request_Documentation 
        fields = '__all__'
    
                
      
class LeadManagementsSerializer(serializers.ModelSerializer):
    
    sources_of_leads = serializers.CharField(required=False)
    bussiness_name = serializers.CharField(required=False)
    bussiness_type = serializers.CharField(required=False)
    contact_number = serializers.IntegerField(required=False)      
    alternate_contact_number = serializers.IntegerField(required=False)
    contact_person = serializers.CharField(required=False) 
    call_connected = serializers.CharField(required=False) 
    state =  serializers.CharField(required=False)
    city =  serializers.CharField(required=False)  
    full_address = serializers.CharField(required=False)
    address =  serializers.CharField(required=False) 
    email = serializers.EmailField(required=False)
    remarks = serializers.CharField(required=False)
    client_behaviour = serializers.IntegerField(required=False)
 
    
    class Meta:
        model = lead_managements
        fields = ['sources_of_leads','bussiness_name','bussiness_type','contact_number','alternate_contact_number','call_connected','contact_person','state','city','full_address','email','remarks','client_behaviour','emp_code']
        
    def create(self, validated_data):
    
        request_data = lead_managements.objects.create(
            sources_of_leads=validated_data.get('sources_of_leads'),
            bussiness_name=validated_data.get('bussiness_name'),
            bussiness_type = validated_data.get('bussiness_type'),
            contact_number = validated_data.get('contact_number'),
            alternate_contact_number=validated_data.get('alternate_contact_number'),
            call_connected = validated_data.get('call_connected'),
            contact_person=validated_data.get('contact_person'),
            state=validated_data.get('state'),
            city=validated_data.get('city'),
            full_address=validated_data.get('full_address'),
            email = validated_data.get('email'),
            remarks = validated_data.get('remarks'),
            client_behaviour=validated_data.get('client_behaviour'),
            emp_code=validated_data.get('emp_code')
            
        )
        return request_data   
        

class LeadManagementsDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = lead_managements 
        fields = '__all__'