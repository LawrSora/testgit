from controllers.controller import Controller

class ArticlesController(Controller):

    def index(self, request, response):
        response.text = self.view.render_html('articles/index.html', {'title': 'статьи', 'h1' : 'статьи на сайте'})

    def view(self, request, response, id):
        article = Article.get_by_id(Article)
        response.text = self.view.render_html('articles/index.html', {'title' : f'MVC framework - {article.name}', 'h1' : f'Статья: {article.name}', 
    'article' : article})

