from django.utils.deprecation import MiddlewareMixin

class setResponse(MiddlewareMixin):
    
    def process_response(self,request,response):  
        # 4.�����и��ݹ������󣬴������������࣬��д����㷽��
        
        response['Cache-Control'] = 'no-cache'
    	response['X-Frame-Options'] = 'ALLOW-FROM'
        return response
