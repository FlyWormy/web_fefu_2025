from django.http import HttpResponse

def bad_request_handler(request, exception):
    return HttpResponse("400 - Bad Request", status=400)

def permission_denied_handler(request, exception):
    return HttpResponse("403 - Permission Denied", status=403)

def page_not_found_handler(request, exception):
    return HttpResponse("404 - Page Not Found", status=404)

def server_error_handler(request):
    return HttpResponse("500 - Server Error", status=500)