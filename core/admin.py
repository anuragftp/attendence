from django.contrib import admin
from core.models import Attendence , Leave , AnnualLeave

# Register your models here.

class AttendenceAdmin(admin.ModelAdmin):
	model=Attendence
	list_display=('id','user','check_in','check_out','working_hours','date')



class LeaveAdmin(admin.ModelAdmin):
	model=Leave
	list_display=('id','leave_type','state','reason','maxleave','user','created_on','updated_on')




class AnnualLeaveAdmin(admin.ModelAdmin):
	model=AnnualLeave
	list_display=('id','holiday_name','start_date','end_date','month','created_on','updated_on')


admin.site.register(Leave, LeaveAdmin)
admin.site.register(Attendence, AttendenceAdmin)
admin.site.register(AnnualLeave, AnnualLeaveAdmin)
