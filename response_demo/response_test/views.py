from django.http import (
    HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse,
    FileResponse, HttpResponseNotFound, HttpResponseBadRequest,
    HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError
)

def simple_response(request):
    return HttpResponse("This is a simple HTTP response.")

def redirect_response(request):
    return HttpResponseRedirect('/responses/simple/')

def json_response(request):
    data = {'key': 'value'}
    return JsonResponse(data)

def file_response(request):
    filename = 'C:/Users/Bastien/Downloads/Packet Sniffing and Wireshark 02.pdf'
    return FileResponse(open(filename, 'rb'), as_attachment=True)

def streaming_response(request):
    def data_stream():
        yield "Hello "
        yield "World!"
    return StreamingHttpResponse(data_stream())

def not_found_response(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def bad_request_response(request):
    return HttpResponseBadRequest('<h1>Bad Request</h1>')

def forbidden_response(request):
    return HttpResponseForbidden('<h1>Forbidden</h1>')

def method_not_allowed_response(request):
    return HttpResponseNotAllowed('<h1>Method Not Allowed</h1>')

def server_error_response(request):
    return HttpResponseServerError('<h1>Internal Server Error</h1>')


