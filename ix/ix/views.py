from django.shortcuts import render

def processing(request):
    # Define the path to your p5.js script
    p5js = 'js/sketch.js'

    # Define the context data to pass to the template
    context = {
        'p5js': p5js,
    }

    # Render the template with the context data
    return render(request, 'p5js/processing.html')