from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render

def home(request):
    number_result = None
    name_filter_result = None

    # Check for number form submission
    if 'number' in request.GET:
        number = request.GET['number']
        if number.isdigit():
            number = int(number)
            if number % 2 == 0:
                number_result = f"{number} is an even number"
            else:
                number_result = f"{number} is an odd number"
        else:
            number_result = "Please enter a valid number"

    # Check for name filter submission
    if 'character' in request.GET:
        character = request.GET['character']
        names = ["hello", "hai", "apple", "banana"]
        name_filter_result = [name for name in names if name.startswith(character)]
  
    return render(request, 'home.html', {
        'number_result': number_result,
        'name_filter_result': name_filter_result,
    })
