from controllers.controller import Controller

class SiteController(Controller):

    def index(self, request, response):
        response.text = self.view.render_html('site/index.html', {'title': 'MVC framework', 'h1' : 'Главная страница'})
    
    def about(self, request, response):
        response.text = self.view.render_html('site/about.html', {'title': 'MVC framework - About', 'h1' : 'О нас'})

class TestController(Controller):
    def __init__(self):
        self.layout = "default"
        self.view = View(self.layout)

    def test(self, request, response):
        response.text = self.view.render_html('site/test.html', {'title': 'test', 'h1' : 'test'})
        
    def action(self, request, response):
        response.text = self.view.render_html('site/action.html', {'title': 'action', 'h1' : 'action'})

    def hello(self, request, response):
        response.text = self.view.render_html('site/hello.html', {'title' : 'MVC фреймворк приветствие', 'h1': 'Привет!', 'user': user_name})
