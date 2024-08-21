from django.shortcuts import render, redirect
from .models import Parent, Student
from .forms import StudentForm
from django.http import HttpResponse


from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is your home page!")


def Students_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            parent = Parent.objects.create(name="ABDULLAHI USMAN", occupation="Backend Engineer")
            student = form.save(commit=False)
            student.parent = parent
            student.save()
            return HttpResponse("Saved Successfully")
        else:
            return redirect('StudentList')  # Redirects if the form is not valid (this logic could be adjusted)

    else:
        form = StudentForm()

    # Render the form
    context = {'form': form}
    return render(request, 'CreateStudent.html', context)



def Student_List(request):
    students = Student.objects.all()
    return render(request, 'StudentList.html', {'students': students})

   