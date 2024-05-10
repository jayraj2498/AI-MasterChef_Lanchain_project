from django.shortcuts import render, redirect
from django.views import View
from jarvischef.forms import RecipeForm
from jarvischef.langchain import askJarvisChef

class Home(View):
    def get(self, request):
        form = RecipeForm()
        return render(request, 'jarvischef/home.html', {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data['recipe_message']
            response = askJarvisChef(recipe_message)
            response_text = response.content  # Get the content of the AIMessage as a string
            request.session['response'] = response_text  # Store the string in the session
            form = RecipeForm()
        return render(request, 'jarvischef/home.html', {'form': form})