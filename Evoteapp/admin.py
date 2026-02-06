from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Login_model)
admin.site.register(User_model)
admin.site.register(Candidate_model)
admin.site.register(Feedback_model)
admin.site.register(Complaint_model)
admin.site.register(Vote_model)
admin.site.register(Officer_model)
admin.site.register(Candidatecode_model)
admin.site.register(Ward)
admin.site.register(UserGroupMapping)
admin.site.register(UserGroup)
admin.site.register(UserCandidateCode)
admin.site.register(Vote)
admin.site.register(Publishstatus)
admin.site.register(Votingtime)