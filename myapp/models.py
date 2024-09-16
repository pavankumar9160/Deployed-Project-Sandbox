# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

import random
import string


class UserManager(BaseUserManager):
    def create_user(self, empcode, empname, password=None, **extra_fields):
        if not empcode:
            raise ValueError('The employee code field must be set')
        user = self.model(empcode=empcode, empname=empname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, empname, password=None, **extra_fields):
        empcode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Generate 6-digit code
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_superuser', True)  # Ensure superuser flag is set

        return self.create_user(empcode, empname, password, **extra_fields)


class ConcreteUser(AbstractBaseUser, PermissionsMixin):
    EMPLOYEE_STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    ]
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    empcode = models.CharField(max_length=10, unique=True)
    empname = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128 , null=True)
    rolename = models.CharField(max_length=50)
    createdby = models.CharField(max_length=50)
    jn_date = models.DateField(null=True, blank=True)
    lv_date = models.DateField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mail_id = models.EmailField(max_length=50, unique=True)
    external_mail = models.EmailField(max_length=50, null=True, blank=True)
    personal_mail = models.EmailField(max_length=50, null=True, blank=True)
    mail_indi = models.CharField(max_length=50, null=True, blank=True)
    gndr = models.IntegerField(choices=GENDER_CHOICES, default=1)
    QMS = models.BooleanField(default=True)
    SAP = models.BooleanField(default=True)
    crnt_sts = models.IntegerField(choices=EMPLOYEE_STATUS_CHOICES, default=1)
    mgr = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    phno = models.CharField(max_length=15, null=True, blank=True)
    loc = models.CharField(max_length=50, null=True, blank=True)
    empgroup = models.CharField(max_length=20, null=True, blank=True)
    empsubgroup = models.CharField(max_length=20, null=True, blank=True)
    payscale_grade = models.CharField(max_length=20, null=True, blank=True)
    payscale_level = models.CharField(max_length=20, null=True, blank=True)
    payscale_sub_level = models.CharField(max_length=20, null=True, blank=True)
    pay_range = models.CharField(max_length=20, null=True, blank=True)
    adapt = models.CharField(max_length=20, null=True, blank=True)
    empType = models.CharField(max_length=50, null=True, blank=True)
    extn = models.CharField(max_length=50, null=True, blank=True)
    shrt = models.CharField(max_length=50, null=True, blank=True)
    active_name = models.CharField(max_length=10, null=True, blank=True)
    photo_sts = models.BooleanField(default=False)
    build_no = models.CharField(max_length=10, null=True, blank=True)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    local_std_code = models.CharField(max_length=10, null=True, blank=True)
    sys_no = models.CharField(max_length=15, null=True, blank=True)
    loc_outstn = models.CharField(max_length=50, null=True, blank=True)
    gl = models.CharField(max_length=60, null=True, blank=True)
    tl = models.CharField(max_length=50, null=True, blank=True)
    level_1 = models.CharField(max_length=50, null=True, blank=True)
    level_2 = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    tprog = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    delete1 = models.BooleanField(default=False)
    marital_status = models.IntegerField(choices=[(0, 'Single'), (1, 'Married')], default=0)
    tms_status = models.BooleanField(default=False)
    ass_role = models.CharField(max_length=10, null=True, blank=True)
    qualification = models.CharField(max_length=20, default='SSC', null=True, blank=True)
    empcode_md5 = models.CharField(max_length=50, null=True, blank=True)
    tr_facility = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    marriage_date = models.DateField(null=True, blank=True)
    phone_permission = models.CharField(max_length=20, default='0')
    bus_route = models.CharField(max_length=10, null=True, blank=True, default='0')
    ext_status = models.CharField(max_length=10, null=True, blank=True)
    work_loc = models.CharField(max_length=50, null=True, blank=True)
    audit_emp_sts = models.CharField(max_length=50, null=True, blank=True)
    auditor_qua_date = models.DateField(null=True, blank=True)
    auditor_disqua_date = models.DateField(null=True, blank=True)
    uan = models.CharField(max_length=20, null=True, blank=True)
    pan = models.CharField(max_length=20, null=True, blank=True)
    bank_indi = models.CharField(max_length=500, null=True, blank=True)
    bank_name = models.CharField(max_length=500, null=True, blank=True)
    bank_ifsc = models.CharField(max_length=500, null=True, blank=True)
    bank_holder_name = models.CharField(max_length=500, null=True, blank=True)
    bank_acc = models.CharField(max_length=500, null=True, blank=True)
    ip_address = models.CharField(max_length=500, null=True, blank=True)
    current_address = models.CharField(max_length=500, null=True, blank=True)
    aadhar_number = models.CharField(max_length=500, null=True, blank=True)
    attendance_status = models.CharField(max_length=10, null=True, blank=True)
    ess = models.CharField(max_length=10, null=True, blank=True)
    alt_contact = models.CharField(max_length=20, null=True, blank=True)
    ot_flag = models.CharField(max_length=20, null=True, blank=True)
    rsc = models.CharField(max_length=2, null=True, blank=True)
    emp_cat = models.CharField(max_length=20, null=True, blank=True)
    
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    pan_card_image = models.ImageField(upload_to='documents/pan_cards/', null=True, blank=True)
    aadhar_card_image = models.ImageField(upload_to='documents/aadhar_cards/', null=True, blank=True)


    USERNAME_FIELD = 'mail_id'
    REQUIRED_FIELDS = ['empname']

    objects = UserManager()

    def __str__(self):
        return self.empname

    class Meta:
        db_table = 'user_master'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Raise_Request_Documentation(models.Model):
    
    REQUEST_TYPE_CHOICES = [
        (1, 'Error'),
        (2, 'Authorization'),
        (3, 'Additions/Improvement'),
        (4, 'New Report'),
        (5, 'New Project'),
        (6, 'Project New Version')
    ]
    
    
    MODULE_TYPE_CHOICES = [
        (1, 'Internal'),
        (2, 'External')
    ]
    
    APPROVE_STS_CHOICES = [
         (0, 'Pending'),
         (1, 'Approved'),
         (2, 'Rejected')    
    ]
    
    USER_STATUS_CHOICES = [
         (0, 'Inactive'),
         (1, 'Active')  
    ]
    
    TAG_CONFIRM_TYPE_CHOICES =[
        
         (1, 'Approved'),
         (2, 'Clarification needed'),
         (3, 'Skipped'),
         (4, 'Tag assigned for developer for future work'),
         
    ]
    
    APPROVE_TYPE_CHOICES =[
        (1,'Waiting for approval'),
        (2, 'approved')
    ]
    
    HD_APP_STS_CHOICES =[
         (1, 'Pending'),
         (2, 'Approved'),
         (3,'Rejected'),
         (4, 'Clarification needed'),
         (5, 'Skipped'),
    ]
    
    USR_STS_CHOICES=[
        (1,'Active'),
        (2,'Inactive')
    ]
 
    
    id = models.AutoField(primary_key=True)
    rqstnr = models.CharField(max_length=500,null=True, blank=True)
    desc = models.CharField(max_length=500, null=True, blank=True)
    rqstd_date = models.DateField(null=True, blank=True)
    rqstd_date_time = models.DateTimeField(auto_now_add=True)
    module = models.IntegerField(choices=MODULE_TYPE_CHOICES,default=0)
    approve_type = models.IntegerField(choices=APPROVE_TYPE_CHOICES,default=1)
    approve_by  = models.CharField(max_length=10, null=True, blank=True)
    hd_app_sts = models.IntegerField(choices=HD_APP_STS_CHOICES,default=1)
    approve_sts = models.IntegerField(choices=APPROVE_STS_CHOICES,default=0)
    approve_timestamp= models.DateTimeField(auto_now_add=True)
    hd_app_date = models.DateTimeField(auto_now_add=True)
    usr_sts = models.IntegerField(choices=USER_STATUS_CHOICES,default=1)
    delete1 = models.BooleanField(default=0, null=True, blank=True)
    tag_confirm_type = models.IntegerField(choices=TAG_CONFIRM_TYPE_CHOICES,default=1)
    attach_file_original = models.ImageField(upload_to='attachments/',null=True, blank=True)
    attach_file_rename = models.ImageField(null=True, blank=True)
    dept = models.CharField(max_length=500, null=True, blank=True)
    reqt_type = models.IntegerField(choices=REQUEST_TYPE_CHOICES,default=0)
    rmrks = models.CharField(max_length=500, null=True, blank=True) 
    
    
    def __str__(self):
        return self.rqstnr
    
    
class main_tr_nd_histry(models.Model):
    
    index = models.AutoField(primary_key=True)
    main_tr_slno = models.IntegerField(null=True,blank=True)
    resp = models.IntegerField(default=0)
    user = models.CharField(max_length=500,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    remarks = models.CharField(max_length=500,default='Created')
    createdby = models.CharField(max_length=500,null=True,blank=True)
    delete1 = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
        
        
class lead_managements(models.Model):
    
    
    CLIENT_BEHAVIOUR_CHOICES =[
        
        (1,'Positive'),
        (2,'Negative'),
        (3, 'Neutral'),
        (4, 'Others')
    ]
    
    id = models.AutoField(primary_key=True)
    sources_of_leads = models.CharField(max_length=500,null=True,blank=True)
    bussiness_name = models.CharField(max_length=500,null=True,blank=True)
    bussiness_type = models.CharField(max_length=500,null=True,blank=True)
    contact_number = models.IntegerField(max_length=10,null=True,blank=True)      
    alternate_contact_number = models.IntegerField(max_length=10,null=True,blank=True)
    call_connected =  models.CharField(max_length=100,null=True,blank=True) 
    contact_person = models.CharField(max_length=500,null=True,blank=True)  
    state =  models.CharField(max_length=100,null=True,blank=True)
    city =  models.CharField(max_length=100,null=True,blank=True)  
    full_address =  models.CharField(max_length=500,null=True,blank=True) 
    email = models.EmailField(max_length=200,null=True,blank=True)
    remarks = models.CharField(max_length=500,null=True,blank=True) 
    client_behaviour = models.IntegerField(choices=CLIENT_BEHAVIOUR_CHOICES,default=1)
    emp_code =  models.CharField(max_length=500,null=True,blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.sources_of_leads
        