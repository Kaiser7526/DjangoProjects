from django.shortcuts import render
from myApp.forms import StudentForm

def formView(request):
    if request.method == "POST":
        f = StudentForm(request.POST)  # Instantiate the form with POST data
        if f.is_valid():
            sid = f.cleaned_data['sid']
            sname = f.cleaned_data['sname']
            smarks = f.cleaned_data['smarks']
            splace = f.cleaned_data['place']
            d = {
                'id1': sid,
                'name': sname,
                'marks': smarks,
                'place': splace
            }
            return render(request, 'myApp/output.html', d)
        else:
            # If the form is not valid, render the form with error messages
            d = {'form': f}
            return render(request, 'myApp/input.html', d)
    else:
        f = StudentForm() 
        d = {'form': f}
        return render(request, 'myApp/input.html', d)
