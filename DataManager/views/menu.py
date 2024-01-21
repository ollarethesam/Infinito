from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'DataManager/menu.html', {'text_color': determine_text_color(request.user.bg_color)})

def determine_text_color(hex_color):
    # Extract RGB values from hex color
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Calculate luminance
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

    # Set a threshold (0.5) for luminance, adjust as needed
    return '#000000' if luminance > 0.5 else '#ffffff'