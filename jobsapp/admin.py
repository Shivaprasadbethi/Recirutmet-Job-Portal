from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job, Applicant

# Register Job model
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'type', 'category', 'company_name', 'last_date', 'filled', 'created_at')
    search_fields = ('title', 'company_name', 'category')
    list_filter = ('type', 'category', 'filled')
    ordering = ('-created_at',)

# Register Applicant model
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'created_at')
    search_fields = ('user__username', 'job__title')
    list_filter = ('job',)
    ordering = ('-created_at',)

# Register models with the admin site
admin.site.register(Job, JobAdmin)
admin.site.register(Applicant, ApplicantAdmin)
