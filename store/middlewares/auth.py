from django.shortcuts import redirect
def auth_middleware(get_response):
    def middleware(request):
        print(request.session.get('customer_id'))
        if not request.session.get('customer_id'):
            return redirect('login')
        
        response = get_response(request)
        return response

    return middleware