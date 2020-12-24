from django.http import HttpResponse
import time
class CustomMiddleware(object):
    def __init__(self,get_response):
        print('init')
        self.get_response = get_response

    def __call__(self,request):
        print('call')
        print('request',request)
        response = self.process_request(request)
        if response is None:
            print(self.get_response(request))
            return self.get_response(request)
        return self.process_response(request,response)

    def process_request(self,request):
        if request:
            print('ash')
            request.st=time.time()
            print(request.st)
            return 1
    def process_response(self,request,response):
        if response:
            print('adgah')
            print(response)
            # r=time.time()
            # print(r)
            # print('time taken',(r-request.st)*1000)
            # return HttpResponse(response)
            return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('view')
        return None

    def process_template_response(self, request, response):
        print('template')
        return response

    def process_exception(self,request,response):
        print('exception')
        print(response)
        return HttpResponse(response)