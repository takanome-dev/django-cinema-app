from django.shortcuts import redirect

def home(request):
  # return render(request, 'home.html')
  return redirect('/movies')