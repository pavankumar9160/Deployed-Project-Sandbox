from django.contrib import admin

# Register your models here.

from .models import ConcreteUser,Raise_Request_Documentation, main_tr_nd_histry, lead_managements

admin.site.register(ConcreteUser)
admin.site.register(Raise_Request_Documentation)
admin.site.register(main_tr_nd_histry)
admin.site.register(lead_managements)


