from controllers.controller import Controller
from models.user import User
from exceptions import NotFoundException, InvalidArgumentException


class UsersController(Controller):
    
    def sign_up(self, request, response):
        
        if request.method == 'POST':
            try:
               user = User.sign_up(request.POST)
               if isinstance(user, User):
                   response.text = self.view.render_html('users/signUpSuccess.html')
                   return
            except InvalidArgumentException as e:
               response.text = self.view.render_html('users/sign_up.html',
               {'title':'MVC framework - регистрация', 'error' : e})
               return 
    
    def sign_in(self, request, response):
        response.text = self.view.render_html('users/sign_in.html',
        {'title':'MVC framework - вход', 'error' : e})
