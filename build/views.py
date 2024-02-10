import django.utils.html
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse


# Create your views here.
def workspace (request):
    return render(request, 'build/workspace.html', {'title':"Workspace"})

def runcode (request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method')

    code = request.POST.get('code', '')
    # Sanitize and escape code string using django.utils.html.escape(...) or similar
    safe_code = django.utils.html.escape(code)

    # Implement your code execution logic here, handling errors and security measures
    try:
        # ... execute code ...
        output = "..."  # Placeholder for execution result
    except Exception as e:
        return HttpResponseBadRequest(f'Error: {e}')

    return HttpResponse(output)