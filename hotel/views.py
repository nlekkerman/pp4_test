from django.http import HttpResponse

def my_view(request):
    response_content = "Hello, World!"  # This could be dynamically generated content
    response = HttpResponse(response_content, content_type="text/plain")
    response["X-My-Header"] = "My Value"
    return response
