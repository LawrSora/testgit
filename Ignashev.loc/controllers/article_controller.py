from controllers.controller import Controller
from models.article import Article
from exceptions import NotFoundExceptions


class ArticlesController(Controller):
    def index (self, request, response):
      articles = Article.find_all()
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework - articles',
        'h1' : 'articles on site',
        'articles' : articles
      })

    def view(self, request, response, id):
       article = Article.get_by_id(id)
       if article is None:
           raise NotFoundExceptions('статья не найдена')
       response.text = self.view.render_html('articles/view.html', 
      {
        'title': f'MVC Framework - {id}',
        'h1' : f'Post',
        'article' : article
      })
       
    def edit(self, request, response, id):
       article = Article.get_by_id(id)
       if article is None:
          response.status_code = 404
          response.text = self.view.render_html('errors/404.html', {
             'error': 'статья не найдена'
          })
          return
       if request.method == 'POST':
          article.set_name(request.POST['name'])
          article.set_name(request.POST['text'])
          article.save()
          response.status_code = 302
          response.headers = [('Location', f'/article/{article.get_id()}')]
          return
       response.text = self.view.render_html('articles/edit.html', 
      {
        'title': f'Редакирование - {article.get_name()}',
        'article' : article
      })
       
    def delete(self, request, response, id):
       article = Article.get_by_id(id)
       if article is None:
          response.status_code = 404
          response.text = self.view.render_html('errors/404.html', {
             'error': 'статья не найдена'
          })
          return
       article.delete()
       response.status_code = 302
       response.headers = [('Location', '/articles')]

    def add(self, request, response):
      article = Article()
      article.set_author_id(1)
      article.set_name('')
      article.get_text()
      article.save()