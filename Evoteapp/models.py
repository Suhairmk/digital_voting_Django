from django.db import models
import uuid
# Create your models here.
from django.utils.timezone import now
from datetime import timedelta
import hashlib
from django.utils.crypto import get_random_string
# Create your models here.
class Login_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
class Ward(models.Model):
    name = models.CharField(max_length=100)
class User_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    mailid = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    mobno = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(upload_to='photo/', null=True, blank=True)
    aadhaar = models.CharField(max_length=100, null=True, blank=True)
    voterid = models.CharField(max_length=100, null=True, blank=True)
    ward =models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,blank=True)
    voter_status = models.BooleanField(default=False)

class Casefile_model(models.Model):
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    caseid = models.CharField(max_length=100, null=True, blank=True)
    crime=models.CharField(max_length=100,null=True,blank=True)
    adhaar_number=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    photo=models.FileField(upload_to='criminals/', null=True, blank=True)
    
    


class Candidate_model(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True)
    mname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True)   
    gender = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    party = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(upload_to='photo/', null=True, blank=True)
    aadhaar = models.CharField(max_length=100, null=True, blank=True)
    proof = models.FileField(upload_to='proof/', null=True, blank=True)
    voterid = models.FileField(upload_to='voterid/', null=True, blank=True)
    phone= models.CharField(max_length=100, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    ward =models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)

class Candidatecode_model(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    candidate = models.ForeignKey(Candidate_model, on_delete=models.CASCADE, null=True, blank=True)
    voter = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    ward =models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,blank=True)

class UserGroup(models.Model):
    group_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

class UserGroupMapping(models.Model):
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE)

class UserCandidateCode(models.Model):
    user = models.ForeignKey(User_model, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate_model, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=10, unique=True)
class Feedback_model(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User_model,on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)


class Complaint_model(models.Model):
    complaint = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User_model,on_delete=models.CASCADE, null=True, blank=True)
    date  = models.DateField(max_length=100, null=True, blank=True)

class Vote_model(models.Model):
    candidate = models.ForeignKey(Candidate_model,on_delete=models.CASCADE, null=True, blank=True)
    vote = models.ForeignKey(User_model,on_delete=models.CASCADE, null=True, blank=True)

class Officer_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True)
    phone= models.CharField(max_length=100, null=True, blank=True)
    mailid = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(upload_to='photo/', null=True, blank=True)
    
# class Login_model(models.Model):
#     username = models.CharField(max_length=100, null=True, blank=True)
#     password = models.CharField(max_length=100, null=True, blank=True)
#     type = models.CharField(max_length=100, null=True, blank=True)

class Votingtime(models.Model):
    electiondate=models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
  

import hashlib


class Vote(models.Model):
    vote_id = models.CharField(max_length=100, unique=True, editable=False)
    voter = models.OneToOneField(User_model, on_delete=models.CASCADE)  # Prevent multiple votes
    candidate = models.ForeignKey(Candidate_model, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_hash = models.CharField(max_length=64, blank=True, null=True)  # Link to previous vote
    vote_hash = models.CharField(max_length=64, blank=True, editable=False)  # Current vote's hash

    def save(self, *args, **kwargs):
        # Generate vote ID
        if not self.vote_id:
            self.vote_id = get_random_string(length=16)
        
        # Generate hash of the current vote
        vote_data = f"{self.vote_id}{self.voter.id}{self.candidate.id}{self.timestamp}"
        self.vote_hash = hashlib.sha256(vote_data.encode()).hexdigest()

        # Assign the previous hash
        if not self.previous_hash:
            last_vote = Vote.objects.order_by('-timestamp').first()
            self.previous_hash = last_vote.vote_hash if last_vote else None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vote by {self.voter.name} for {self.candidate.fname}"
    




class Publishstatus(models.Model):
    STATUS_CHOICES = [
        ('true', 'Publish'),
        ('false', 'Unpublish'),
    ]
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='false')