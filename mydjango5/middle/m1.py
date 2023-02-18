from django.utils.deprecation import MiddlewareMixin

class setResponse(MiddlewareMixin):
    
    def process_response(self,request,response):  
        # 4.在类中根据功能需求，创建切入需求类，重写切入点方法
        
        response['Cache-Control'] = 'no-cache'
    	response['X-Frame-Options'] = 'ALLOW-FROM'
        return response
