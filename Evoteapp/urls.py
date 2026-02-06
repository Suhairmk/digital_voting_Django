
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', Login.as_view(),name='login'),
    path('logout/', logout.as_view(),name='logout'),
    path('dash', AdminDash.as_view(),name='dash'),
    path('offdash', Officerdash.as_view(),name='offdash'),
    path('Addcasefiles',Addcasefiles.as_view(),name='Addcasefiles'),
    path('Addwards',Addwards.as_view(),name='Addwards'),
    path('ElectionDeclare',ElectionDeclare.as_view(),name='ElectionDeclare'),
    path('publishStatus',PublishStatus.as_view(),name='publishStatus'),

    path('insertcandidate', Insertcandidate.as_view(),name='insertcandidate'),
    path('editcandidate/<int:c_id>', Editcandidate.as_view(),name='editcandidate'),
    path('deletecandidate/<int:c_id>', Deletecandidate.as_view(),name='deletecandidate'),
    path('complaints', Complaints.as_view(),name='complaints'),
    path('feedback', Feedback.as_view(),name='feedback'),
    path('standings', Standings.as_view(),name='standings'),
    path('participants', participants.as_view(),name='participants'),
    path('managecandidate', Managecandidate.as_view(),name='managecandidate'),
    path('officerlogin', Officerlogin.as_view(),name='officerlogin'),
    path('officerdash', Officerdash.as_view(),name='officerdash'),
    path('regvoters', Registeredvoters.as_view(),name='regvoters'),
    path('candidates', candidates.as_view(),name='candidates'),
    path('viewvoters/<int:u_id>', viewvoters.as_view(),name='viewvoters'),
    path('candetails', Candedatedetails.as_view(),name='candetails'),
    path('results', Results.as_view(),name='results'),
    path('qualifiedc', qualifiedc.as_view(),name='qualifiedc'),
    path('seecandidate/<int:c_id>', viewcandidate.as_view(),name='seecandidate'),
    path('Verifyuser/<int:id>',Verifyuser.as_view(),name='verifyuser'),
    path('Verifycandidate/<int:id>',verifycandidate.as_view(),name='verifycandidate'),
    path('Rejectcandidate/<int:id>',rejectcandidate.as_view(),name='rejectcandidate'),

    path('candidatesapi/', CandidateAPIView.as_view(), name='candidates-list-create'),
    path('candidatesapi/<int:pk>/', CandidateAPIView.as_view(), name='candidate-detail-update'),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback-list'),
    # path('feedback/<int:pk>/', FeedbackAPIView.as_view(), name='feedback-detail'),
    path('complaints/', ComplaintAPIView.as_view(), name='complaint-list'),
    # path('complaints/<int:pk>/', ComplaintAPIView.as_view(), name='complaint-detail'),
    path('votes/', VoteAPIView.as_view(), name='vote-list'),
    path('votes/<int:pk>/', VoteAPIView.as_view(), name='vote-detail'),
    path('officers/', OfficerAPIView.as_view(), name='officer-list-create'),
    path('officers/<int:pk>/', OfficerDetailAPIView.as_view(), name='officer-detail-update'),
    path('userregistration', UserAPIView.as_view(), name='user-list-create'),
    path('userregistration/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    # path('candidate-codes/', CandidateCodeAPIView.as_view(), name='candidate_codes'),
    # path('candidate-codes/<int:pk>/', CandidateCodeDetailAPIView.as_view(), name='candidate_code_detail'),
    path('logincheck/', LoginPage.as_view(), name='logincheck'),  # ✅ Correct
    # path('create-groups/', CreateUserGroupsView.as_view(), name='create_groups'),
    # path('process-group/', ProcessGroupView.as_view(), name='process_group'),
    # path("groups/", group_list_view, name="group-list"),
    # path('generate-codes/<int:group_id>/', GenerateAndSendCodesView.as_view(), name='generate_codes'),
    # path('getcodes/<int:id>',getcodes.as_view(),name='getcodes'),
    path('WardAPIView',WardAPIView.as_view(),name='WardAPIView'),
    

    path("api/vote/", CastVoteAPIView.as_view(), name="cast-vote"),
    path('Result/',Result.as_view(),name='Result'),
    path("api/ward-results/", WardResultAPIView.as_view(), name="ward-results"),
    #/api/ward-results/?login_id=5
    


    

]
