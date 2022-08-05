from django.contrib import admin

# Register your models here.
##from import_export.admin import ImportExportModelAdmin
#from import_export.widgets import ForeignKeyWidget
from import_export import fields, resources
##from import_export import resources
#from .models import Transaction, Reconciliation
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Upload, Seat, Aspirant, User, Vote, Votecast


#admin.site.register(Upload)
#class UploadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 #       ...     
#admin.site.register(Upload, UploadAdmin) 
class UploadResource(resources.ModelResource):
	class Meta:
		model = Upload
       # import_id_fields = ('Transaction_id',)
	fields = ('county', 'const', 'ward', 'center', 'voters', 'pstation')
	list_filter = ('ward')

class UploadAdmin(ImportExportModelAdmin):
    resource_class = UploadResource

admin.site.register(Upload, UploadAdmin)
admin.site.register(Seat)
admin.site.register(Aspirant)
admin.site.register(User)
admin.site.register(Vote)
admin.site.register(Votecast)

'''
class GpaymentResource(resources.ModelResource):
	class Meta:
		model = Gpayment
       # import_id_fields = ('Transaction_id',)
	fields = ('id', 'owner', 'status', 'amount', 'pending', 'balance')
	list_filter = ('owner')

class GpaymentAdmin(ImportExportModelAdmin):
    resource_class = GpaymentResource

admin.site.register(Gpayment, GpaymentAdmin)

class TestResource(resources.ModelResource):
	class Meta:
		model = Test
       # import_id_fields = ('Transaction_id',)
	fields = ('id', 'name', 'room')
	list_filter = ('room')

class TestAdmin(ImportExportModelAdmin):
    resource_class = TestResource

admin.site.register(Test, TestAdmin)

'''


