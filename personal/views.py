from django.shortcuts import render

def home_screen_view(request):

    context = {}
    list_of_value = []
    list_of_value.append('first')
    context['list_of_values'] = list_of_value
    return render(request, 'index.html',context)
