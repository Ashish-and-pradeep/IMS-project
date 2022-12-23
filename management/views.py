from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Student,Teacher,Course,Teachers,Gall,Content
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    teacher=Teachers.objects.all()
    course=Course.objects.all()
    data={}
    data['teacher']=teacher
    data['course']=course
    return render(request,"index.html",data)
def about(request):
    return render(request,"about.html")
def register(request):
    if request.method=="POST":
        err=None
        name=request.POST.get('name')
        branch=request.POST.get('branch')
        type=request.POST.get('type')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        image=request.POST.get('image')

        if type=='Student':
           data=Student(name=name,branch=branch,email=email,password=passw,address=address,gender=gender,image=image)
        elif type=='Teacher':
           data=Teacher(name=name,branch=branch,email=email,password=passw,contact=1234,address=address,gender=gender,image=image)
        else:
            err='Please Select User type !.'
        if not name.isalpha():
            err='Invalid name ! Please enter right name...'
        if data.is_exists():
            err='Email ! Already exist..'
        if err:
            return render(request,'register.html',{'err':err})
        data.save()
        # Create user
        myuser=User.objects.create_user(username=email,password=passw)
        myuser.save()

        err='Successfully Registered ! Try to Loging in '
        return render(request,'login.html',{'err':err})
    return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        type=request.POST.get('type')
        myuser=authenticate(username=email,password=password)
        if myuser is not None:
            login(request,myuser)
            try:
                if type=='Student':
                    stu=Student.objects.filter(request.user.username)
                else:
                    stu = Teacher.objects.filter(request.user.username)
            except Exception as e:
                print(e)
                stu=[]
            request.session['stu']=stu
            if type=='Student':
                return redirect('student')
            else:
                return redirect('teacher')
        else:
            msg="Incorrect Id or password"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')

@login_required(redirect_field_name='index')
def student(request):

    detail=Student.get_data_by_email(request.user.username)
    cont=Content.objects.all()
    data={}

    data['detail']=detail
    data['cont']=cont
    return render(request,'student.html',data)
@login_required(redirect_field_name='index')
def teacher(request):
    detail = Teacher.get_data_by_email(request.user.username)
    data={}
    data['detail']=detail
    return render(request,'teacher.html',data)
def singout(request):
    logout(request)
    request.session.flush()
    return redirect('index')


def gellery(request):
    gall=Gall.objects.all()
    return render(request,"gallery.html",{'gallery':gall})
def notes(request):
    if request.method=='POST':
        name=request.POST['tname']
        sub=request.POST['sub']
        note=request.FILES['notes']

        con=Content(name=name,subject=sub,content=note)
        con.save()

    return redirect('teacher')