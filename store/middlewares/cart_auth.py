from django.shortcuts import redirect, HttpResponseRedirect

def cart_middleware(get_response):

    def middleware(request):
        if not request.session.get('cart'):
            print(request.session.get('cart'))
            return redirect('home')
        else:
            response = get_response(request)
            return response
    
    return middleware