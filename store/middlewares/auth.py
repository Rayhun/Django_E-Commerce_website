from django.shortcuts import redirect, HttpResponseRedirect

def auth_middleware(get_response):

    def middleware(request):
        # returnUrl = request.META['PATH_INFO']
        # print(returnUrl)
        if not request.session.get('customer_id'):
            # print(redirect(f'login?return_url={returnUrl}'))
            return redirect('login')
        else:
            response = get_response(request)
            return response
    
    return middleware