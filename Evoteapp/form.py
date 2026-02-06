from django.forms import ModelForm

from Evoteapp.models import Candidate_model, Casefile_model, Complaint_model, Feedback_model, Login_model, Officer_model, Publishstatus, User_model, Vote_model, Votingtime, Ward


class Candidate_modelForm(ModelForm):
    class Meta:
        model = Candidate_model
        fields=['fname','mname','lname','dob','gender','address','party','ward','logo','city','state','country','pincode','photo','aadhaar','proof','voterid','phone','mail']

class Login_modelform(ModelForm):
    class Meta:
        model = Login_model
        fields=['username','password','type']

class User_modelform(ModelForm):
    class Meta:
        model = User_model
        fields=['LOGIN_ID','name','gender','dob','mailid','mobno','photo','aadhaar']

class Casefile_modelform(ModelForm):
    class Meta:
        model=Casefile_model
        fields=['name','caseid','crime','adhaar_number','phone','photo']

class Ward_modelform(ModelForm):
    class Meta:
        model=Ward
        fields=['name']
class Feedback_modelform(ModelForm):
    class Meta:
        model = Feedback_model
        fields=['feedback','user','date']
class Complaint_modelform(ModelForm):
    class Meta:
        model = Complaint_model
        fields=['complaint','user','date']
class Vote_modelform(ModelForm):
    class Meta:
        model = Vote_model
        fields=['candidate','vote']
class Officer_modelform(ModelForm):
    class Meta:
        model = Officer_model
        fields=['LOGIN_ID','name','gender','dob','phone','mailid','photo']
       
class Votingtime_modelform(ModelForm):
    class Meta:
        model = Votingtime
        fields=['electiondate','start_time','end_time']
class Publishstatus_modelform(ModelForm):
    class Meta:
        model = Publishstatus
        fields=['status']