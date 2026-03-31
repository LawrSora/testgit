from controllers.controller import Controller
from models.article import Article


class ArticlesController(Controller):
    def index (self, request, response):
      articles = Article.find_all(Article)
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework - articles',
        'h1' : 'articles on site',
        'articles' : articles
      })

    def view(self, request, response, id):
       article = Article.get_by_id(id)
       article = Article.get_by_id(id)
       if article is None:
          response.status_code = 404
          response.text = self.view.render_html('errors/404.html', {
             'error': 'статья не найдена'
          })
          return
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
       response.text = self.view.render_html('articles/edit.html', 
      {
        'title': f'Редакирование - {article.get_name()}',
        'article' : article
      })