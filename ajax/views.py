from django.shortcuts import render
from .models import Person
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request,'ajax/index.html')

def show(request):
    detail=Person.objects.all()
    return JsonResponse({
        'Profile':list(detail.values())
    })

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        major = request.POST['major']
        new = Person(name=name,email=email,major=major)
        new.save()
        return JsonResponse({'message': 'Student added Successfully!'})
    
def edit_student(request, student_id):
    if request.method == 'POST':
        try:
            student = Person.objects.get(id=student_id)
            # Update student fields with the data from the POST request
            student.name = request.POST.get('name')
            student.email = request.POST.get('email')
            student.major = request.POST.get('major')
            # Save the updated student
            student.save()
            # Return updated student data
            data = {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'major': student.major,
            }
            return JsonResponse(data)
        except Person.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    elif request.method=='GET':
        # Handle GET requests for fetching student data if needed
        # Example:
        try:
            student = Person.objects.get(id=student_id)
            data = {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'major': student.major,
            }
            return JsonResponse(data)
        except Person.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

def delete_student(request, student_id):
    if request.method=='POST':
        student = Person.objects.get(id=student_id)
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully!'})  