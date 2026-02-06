from ast import Delete
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import logout
from Evoteapp.form import *
from Evoteapp.models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'Administrator/login.html')
    def post(self, request):
        username_var = request.POST['username']
        password_var = request.POST['password']
        try:
            login_obj = Login_model.objects.get(username=username_var,password=password_var)
            if login_obj.type == "admin":
                return HttpResponse('''<script>alert("Welcome to admin");window.location="/dash";</script>''')
            if login_obj.type == "officer" :
                return HttpResponse('''<script>alert("Welcome to officer");window.location="/officerdash";</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid username or password");window.location="/";</script>''')
        except:
            return HttpResponse('''<script>alert("Invalid username or password");window.location="/";</script>''')

class logout(View):
    def get(self, request):
        logout(request)
        return HttpResponse('''<script>alert("You have been logged out");window.location="/Administrator/login";</script>''')
    
    
class AdminDash(View):
    def get(self, request):
        obj= Vote_model.objects.all()
        obj1=Candidate_model.objects.all()
        obj2=Feedback_model.objects.all()
        obj3=Complaint_model.objects.all()
        obj4=Casefile_model.objects.all()
        obj5=Ward.objects.all()
        result= Publishstatus.objects.filter(id=1).first()
        votetime= Votingtime.objects.filter(id=1).first()
        print("votetime",votetime)
                # Create a dictionary to check if a user has cases based on id_number
        for user in obj1:
            user.has_case = Casefile_model.objects.filter(adhaar_number=user.aadhaar).exists()

        # print(user_cases)


        return render(request, 'Administrator/admindash.html',{'val': obj,'v':obj1,'v1':obj2,'v2':obj3,'v4':obj4,'wards':obj5,'result':result,'votetime':votetime})
    
class Addcasefiles(View):
    def post(self,request):
        form=Casefile_modelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Case file added successfully");window.location="/dash";</script>''')
       

    
class Insertcandidate(View):
    def get(self, request):
        return render(request, 'Officer/officer.html')
    def post(self, request):
        aadhaar_number = request.POST.get('aadhaar')

        # Check if Aadhaar number already exists
        if Candidate_model.objects.filter(aadhaar=aadhaar_number).exists():
            return HttpResponse('''<script>alert("Aadhaar number already exists"); window.location="/offdash";</script>''')

        form = Candidate_modelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Candidate Added Successfully");window.location="/offdash";</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid Form");window.location="/offdash";</script>''')
        
class Deletecandidate(View):
    def get(self, request,c_id):
        obj=Candidate_model.objects.get(id=c_id)
        
        obj.delete()
        return HttpResponse('''<script>alert("Candidate Deleted Successfully");window.location="/offdash";</script>''')
    

        
class Editcandidate(View):
    def get(self, request,c_id):
        obj=Candidate_model.objects.get(id=c_id)
        wards=Ward.objects.all()
    
        return render(request, 'Officer/edit.html',{'val':obj,'wards':wards})
    def post(self, request, c_id):
        obj=Candidate_model.objects.get(id=c_id)
        form = Candidate_modelForm(request.POST,request.FILES ,instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Candidate Edit Successfully");window.location="/offdash";</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location="/offdash";</script>''')
        
class Complaints(View):
    def get(self, request):
        obj= Complaint_model.objects.all()
        return render(request, 'Administrator/complaintss.html',{'val':obj})
    
class Feedback(View):
    def get(self, request):
        obj= Feedback_model.objects.all()
        return render(request, 'Administrator/feedbak.html',{'val': obj})
    
class Managecandidate(View):
    def get(self, request):
        obj= Candidate_model.objects.all()
        return render(request, 'Administrator/admin.html',{'val': obj})
class Addwards(View):
    def post(self,request):
        form=Ward_modelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Ward Added Successfully");window.location="/dash";</script>''')

class ElectionDeclare(View):
    def post(self,request):
        print(request.POST)
        voting_time, created = Votingtime.objects.update_or_create(
        id=1,  # Assumes only one record exists
        defaults={
            'electiondate': request.POST.get('electiondate'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time')
        }
    )

        print(voting_time)
        return HttpResponse('''<script>alert("Election Declared Successfully");window.location="/dash";</script>''')

class PublishStatus(View):


    def post(self,request):
        print(request.POST)
        publish_status, created = Publishstatus.objects.update_or_create(
            id=1,  # You can change this logic if you have multiple entries
            defaults={'status': request.POST.get('status')} 
        )
        print(publish_status)
        return HttpResponse('''<script>alert("Election Declared Successfully");window.location="/dash";</script>''')
        
class Standings(View):
    def get(self, request):
        obj= Vote_model.objects.all()
        return render(request, 'Administrator/standings.html',{'val': obj})
    
class votedisplay(View):
    def get(self, request):
        obj= Vote_model.objects.all()
        return render(request, 'Administrator/admdash.html',{'val': obj})
    
class participants(View):
    def get(self, request):
        obj= Candidate_model.objects.all()
        return render(request, 'Administrator/participants.html',{'val' : obj})
    
class votes(View):
    def get(self, request):
        obj= Vote_model.objects.all()
        return render(request, 'Administrator/standings.html',{'val': obj})
    
class Officerlogin(View):
    def get(self, request):
        return render(request, 'Officer/offlogin.html')
    def post(self, request):
        username_var = request.POST['username']
        password_var = request.POST['password']
        try:
            login_obj = Login_model.objects.get(username=username_var,password=password_var)
            if login_obj.type == "officer":
                return HttpResponse('''<script>alert("Welcome to officer");window.location="/officerdash";</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid username or password");window.location="/";</script>''')
        except:
            return HttpResponse('''<script>alert("Invalid username or password");window.location="/";</script>''')

    
class Officerdash(View):
    def get(self, request):
        obj=Candidate_model.objects.all()
        obj2=User_model.objects.all()
        wards=Ward.objects.all()
                
        


        return render(request, 'Officer/officer.html',{'v1': obj,'v2':obj2,'wards':wards})


    
class candidates(View):
    def get(self, request):
        obj= Candidate_model.objects.all()
        return render(request, 'officer/candidate.html',{'val': obj})
class qualifiedc(View):
    def get(self, request):
        obj= Candidate_model.objects.all()
        return render(request, 'officer/qualifiedc.html',{'val': obj})
    

    
class Registeredvoters(View):
    def get(self, request):
        obj= User_model.objects.all()
        return render(request, 'Officer/registeredvoters.html',{'val': obj})
    
# class Viewvoters(View):
#     def get(self, request,u_id):
#         obj= User_model.objects.get(id=u_id)
#         return render(request, 'Officer/viewvoters.html',{'val': obj})
    
class Candedatedetails(View):
    def get(self, request):
        return render(request, 'Officer/candidatedetails.html')
class Results(View):
    def get(self, request):
        return render(request, 'Officer/result.html')
    
class viewcandidate(View):
    def get(self, request,c_id):
        obj=Candidate_model.objects.get(id=c_id)
    
        return render(request, 'Officer/seecandidate.html',{'val':obj})
    
class viewvoters(View):
    def get(self, request,u_id):
        obj=User_model.objects.get(id=u_id)
    
        return render(request, 'Officer/viewvoters.html',{'val':obj})
    

#API user

    
class UserReg(APIView):
    def POST(self,request):
        print("############### Request Data:", request.data)
        User_serial = userserializer(data=request.data)
        login_serial = loginserializer(data=request.data)

        data_valid = userserializer.is_valid()
        login_valid =loginserializer.is_valid()


        if data_valid and login_valid:
            # hashed_password = make_password(request.data['password'])
            login_profile = loginserializer.save(user_type="USER",password=request.data['password'],username=request.data['username'],status="Active")
            user=userserializer.save(LOGIN_ID=login_profile)

            Warning.objects.create(USERID=user,balance=1000.00)

            response_data={
                "message":" Success",
                "data":userserializer.data
            }
            return Response(response_data, status=status.HTTP_201_OK)

        return Response({
            'login_errors': loginserializer.errors if not login_valid else None,
            'user_errors': userserializer.errors if not data_valid else None
        },status=status.HTTP_400_BAD_REQUEST)


class LoginPage(APIView):

    def post(self, request):
        print("Request body (raw):", request.body)  # Check raw request data
        print("Request data (parsed):", request.data)  # Check parsed data

        username = request.data.get("email")  
        password = request.data.get("password")

        print("Received credentials:", username, password)

        if not username or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Login_model.objects.get(username=username, password=password,status='verified')
            return Response({"task": "Login successful", "user_id": user.id,"type":user.type}, status=status.HTTP_200_OK)
        except Login_model.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CandidateAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            candidate = get_object_or_404(Candidate_model, pk=pk)
            serializer = Candidateserializer(candidate)
        else:
            candidates = Candidate_model.objects.all()
            serializer = Candidateserializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Candidateserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        candidate = get_object_or_404(Candidate_model, pk=pk)
        serializer = Candidateserializer(candidate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # Disable CSRF for APIs
class FeedbackAPIView(APIView):
    def post(self, request, pk=None): 
       
        try:
            LID=request.data['lid']
            user = User_model.objects.get(LOGIN_ID__id=LID)
            print(user)  
        except User_model.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        data={}
        # Add user to request data before saving
        data = request.data
        data["user"] = user.id  # Assign user ID

        serializer = feedbackserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        try:
            feedback = Feedback_model.objects.get(pk=pk)
        except Feedback_model.DoesNotExist:
            return Response({'error': 'Feedback not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = feedbackserializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ComplaintAPIView(APIView):

    def post(self, request, pk=None): 
       
        try:
            LID=request.data['lid']
            print(LID)
            user = User_model.objects.get(LOGIN_ID__id=LID)
            print(user)  
        except User_model.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        data={}
        # Add user to request data before saving
        data = request.data
        print(data)
        data["user"] = user.id  # Assign user ID

        serializer = complaintserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        complaint_id = kwargs.get('pk')  # Get complaint ID from URL
        try:
            complaint = Complaint_model.objects.get(pk=complaint_id)
        except Complaint_model.DoesNotExist:
            return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = complaintserializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VoteAPIView(APIView):
    def get(self, request):
        votes = Vote_model.objects.all()
        serializer = voteserializer(votes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = voteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        vote_instance = get_object_or_404(Vote_model, pk=pk)
        serializer = voteserializer(vote_instance, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WardAPIView(APIView):

    def get(self, request):
        officers = Ward.objects.all()
        serializer = wardserializer(officers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OfficerAPIView(APIView):

    def get(self, request):
        officers = Officer_model.objects.all()
        serializer = Officerserializer(officers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Officerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OfficerDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Officer_model.objects.get(pk=pk)
        except Officer_model.DoesNotExist:
            return None

    def get(self, request, pk):
        officer = self.get_object(pk)
        if officer:
            serializer = Officerserializer(officer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Officer not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        officer = self.get_object(pk)
        if officer:
            serializer = Officerserializer(officer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Officer not found"}, status=status.HTTP_404_NOT_FOUND)


import random
import string


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        print("------------.",data)

        # Extract username and password
        username = data.get("email")
        password = data.get("password")

        # Create a login entry
        login_data = {"username": username, "password": password, "type": "voter", "status": "active"}
        login_serializer = loginserializer(data=login_data)
        print(login_serializer)

        if login_serializer.is_valid():
            login_instance = login_serializer.save()  # Save login entry
        else:
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Generate a random voter ID
        voter_id = ''.join(random.choices(string.digits, k=10)) 
        print(voter_id)

        # Add voter_id and login_instance to user data
        user_data = {
            "LOGIN_ID": login_instance.id,
            "name": data.get("first_name"),
            "gender": data.get("gender"),
            "dob": data.get("dob"),
            "age": data.get("age"),
            "mailid": data.get("email"),
            "address": data.get("address"),
            "mobno": data.get("phone"),
            "photo": data.get("photo"),
            "aadhaar": data.get("aadhar"),
            "voterid": voter_id ,
            'ward':data.get('ward'),
              # Assign generated voter ID
        }
        print(user_data)

        # Serialize and save user data
        user_serializer = userserializer1(data=user_data)
        print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        
        # If user data is invalid, delete created login entry
        login_instance.delete()
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return User_model.objects.get(LOGIN_ID__id=pk)
        except User_model.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = userserializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = userserializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CandidateCodeAPIView(APIView):
    """
    API view for Candidatecode_model to handle GET, POST, and PUT requests.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET request to retrieve all candidate codes"""
        codes = Candidatecode_model.objects.all()
        serializer = CandidateCodeSerializer(codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handles POST request to create a new candidate code"""
        serializer = CandidateCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidateCodeDetailAPIView(APIView):
    """
    API view to handle retrieving and updating a specific candidate code.
    """

    def get_object(self, pk):
        try:
            return Candidatecode_model.objects.get(pk=pk)
        except Candidatecode_model.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        """Handles GET request to retrieve a single candidate code by ID"""
        code = self.get_object(pk)
        if not code:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CandidateCodeSerializer(code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """Handles PUT request to update an existing candidate code"""
        code = self.get_object(pk)
        if not code:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CandidateCodeSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Verifyuser(View):
    def get(self,request,id):
        user=User_model.objects.get(id=id)
        print(user)
        user.LOGIN_ID.status="verified"
        user.LOGIN_ID.save()
        return redirect('officerdash')
    
class verifycandidate(View):
    def get(self,request,id):
        candidate=Candidate_model.objects.get(id=id)
        candidate.status="verified"
        candidate.save()
        return redirect('dash')
class rejectcandidate(View):
    def get(self,request,id):
        candidate=Candidate_model.objects.get(id=id)
        candidate.status="rejected"
        candidate.save()
        return redirect('dash')   
    
import random
from django.views import View
from django.http import JsonResponse
from .models import Candidate_model, User_model, UserCandidateCode, UserGroup, UserGroupMapping
from django.shortcuts import render
from .models import UserGroup

def group_list_view(request):
    groups = UserGroup.objects.all() 
    print(groups) # Fetch all unique groups
    return render(request, "Officer/group_list.html", {"groups": groups})

class CreateUserGroupsView(View):
    def get(self, request, *args, **kwargs):
        users = list(User_model.objects.all())
        random.shuffle(users)
        
        groups_created = []
        for i in range(0, len(users), 10):
            group = UserGroup.objects.create()
            selected_users = users[i:i + 10]
            for user in selected_users:
                UserGroupMapping.objects.create(group=group, user=user)
            groups_created.append(group.group_id)
        return HttpResponse('''<script>alert('Groups generated');location.href='/officerdash'</script>''')
        # return JsonResponse({"status": "Groups Created", "groups": groups_created})
class ProcessGroupView(View):
    def get(self, request, *args, **kwargs):
        group = UserGroup.objects.first()  # Pick the first group available
        if not group:
            return JsonResponse({"status": "No groups available"})

        users_in_group = UserGroupMapping.objects.filter(group=group).values_list('user', flat=True)
        candidates = Candidate_model.objects.filter(ward__in=User_model.objects.filter(id__in=users_in_group).values_list('ward', flat=True))
        
        return JsonResponse({
            "status": "Candidates Retrieved",
            "group_id": str(group.group_id),
            "candidates": list(candidates.values("fname", "aadhaar", "dob", "phone"))
        })

class getcodes(APIView):
    def get(self,request,id):
        usercodes=UserCandidateCode.objects.filter(user__LOGIN_ID__id=id).all()
        ser=UserCandidateCodeserializer(usercodes,many=True)
        return Response(ser.data)


import string
import random

import random
import string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from Evoteapp.models import UserGroup, UserGroupMapping, User_model, Candidate_model, UserCandidateCode

class GenerateAndSendCodesView(View):
    def get(self, request,group_id, *args, **kwargs):
        print("dddddddddd")
        print(f"Generating codes for Group ID: {group_id}")

        group = UserGroup.objects.filter(id=group_id).first()  # Pick first available group
        if not group:
            return JsonResponse({"status": "No groups available"})

        # Get all users in the group with their ward and email
        users_in_group = UserGroupMapping.objects.filter(group=group).values_list('user', flat=True)
        users = User_model.objects.filter(id__in=users_in_group).values('id', 'ward', 'mailid')

        # Create a ward-to-users mapping
        ward_users_map = {}
        email_data = {}

        for user in users:
            ward_users_map.setdefault(user['ward'], []).append(user)

        # Get all candidates in the wards of selected users
        candidates = Candidate_model.objects.filter(ward__in=ward_users_map.keys())
        print(candidates)

        for candidate in candidates:
            print(candidate)
            users_in_ward = ward_users_map.get(candidate.ward_id, [])
            print(users_in_ward)

            for user in users_in_ward:
                print(user)
                unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                UserCandidateCode.objects.create(user_id=user['id'], candidate=candidate, unique_code=unique_code)

                if user['mailid']:  # Ensure user has an email
                    email_data.setdefault(user['mailid'], []).append(f"{candidate.fname}({candidate.party}): {unique_code}")

        # **Send Emails**
        for email, codes in email_data.items():
            send_mail(
                subject="Your Candidate Codes",
                message="\n".join(codes),
                from_email="admin@example.com",
                recipient_list=[email],
            )
        return HttpResponse('''<script>alert('Codes Generated and sent');location.href='/officerdash'</script>''')
        # return JsonResponse({"status": "Codes Generated & Sent"})
from django.utils.timezone import now, localtime
class CastVoteAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        user_id = request.data.get("user_id")
        unique_code = request.data.get("unique_code")

        if not user_id or not unique_code:
            return Response({"error": "Missing user ID or unique code."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            voting_time = Votingtime.objects.first()  # Assuming only one election at a time
            current_datetime = localtime(now()) 

            if not voting_time:
                return Response({"error": "Voting schedule not set."}, status=status.HTTP_400_BAD_REQUEST)

            election_date = voting_time.electiondate
            start_time = voting_time.start_time
            end_time = voting_time.end_time

            if current_datetime.date() != election_date:
                print("ff",current_datetime.date(), election_date)
                return Response({"message": "Election not started or already ended"}, status=status.HTTP_201_CREATED)

            if current_datetime.time() < start_time:
                print("gg",current_datetime.time(), start_time)
                return Response({"message": "Election has not started yet"}, status=status.HTTP_201_CREATED)

            if current_datetime.time() > end_time:
                print("hh",current_datetime.time(), end_time)
                return Response({"message": "Election has ended"}, status=status.HTTP_201_CREATED)
    
        except Votingtime.DoesNotExist:
            return Response({"error": "Election timing not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Validate unique code
        try:
            user_code = UserCandidateCode.objects.get(user__LOGIN_ID__id=user_id, unique_code=unique_code)
            print(user_code)
        except UserCandidateCode.DoesNotExist:
            return Response({"error": "Invalid unique code or user."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate voter
        try:
            voter = User_model.objects.get(LOGIN_ID__id=user_id)
        except User_model.DoesNotExist:
            return Response({"error": "Voter not found!"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the voter has already voted
        if voter.voter_status == True:
            return Response({"message": "You have already voted"}, status=status.HTTP_201_CREATED)

        # Validate candidate
        candidate = user_code.candidate  # Candidate linked to unique code

        # Record the vote
        vote = Vote.objects.create(voter=voter, candidate=candidate)

        # Mark voter as having voted
        voter.voter_status = True
        voter.save()

        # Send confirmation email
        if voter.mailid:
            send_mail(
                "Vote Confirmation",
                "You have successfully cast your vote!",
                "admin@example.com",  # Replace with actual sender email
                [voter.mailid],
            )

        return Response({"message": "Vote cast successfully!"}, status=status.HTTP_201_CREATED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Candidate_model, User_model
import datetime

class WardResultAPIView(APIView):
    def get(self, request, *args, **kwargs):
        login_id = request.query_params.get("login_id")

        if not login_id:
            return Response({"error": "Missing login_id parameter."}, status=status.HTTP_400_BAD_REQUEST)
        publish_status = Publishstatus.objects.first()  # Assuming there is only one publish status record

        if not publish_status or publish_status.status == "false":
            return Response({"message": "Result not published"}, status=status.HTTP_200_OK)

        # Validate voter and get their ward
        try:
            voter = User_model.objects.get(LOGIN_ID__id=login_id)
            voter_ward = voter.ward  # Assuming the VoterTable has a 'ward' field
        except User_model.DoesNotExist:
            return Response({"error": "Voter not found!"}, status=status.HTTP_404_NOT_FOUND)

        # Fetch candidates in the voter's ward with vote counts
        candidates = Candidate_model.objects.filter(ward=voter_ward).annotate(vote_count=Count("vote")).order_by("-vote_count")

        # Prepare results
        result_data = [
            {
                "candidate_id": candidate.id,
                "candidate_name": candidate.fname,  # Assuming 'name' is a field in CandidateTable
                "ward": candidate.ward.name,  # Assuming 'ward' is a ForeignKey to a Ward model
                "vote_count": candidate.vote_count,
                "candidate_image": request.build_absolute_uri(candidate.photo.url) if candidate.photo else None

            }
            for candidate in candidates
        ]

        return Response(
            {"current_time": datetime.datetime.now(), "ward_results": result_data},
            status=status.HTTP_200_OK,
        )
class Result(View):
    def get(self,request):
       current_time = datetime.datetime.now()
       obj = Vote.objects.values('candidate__fname','candidate__ward').annotate(vote_count=models.Count('id')).order_by('-vote_count')
       print(obj)
       return render(request,'Officer/result.html',{'results':obj,'current_time':current_time})      
