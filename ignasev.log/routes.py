from controllers.site_controller import SiteController, TestController
from controllers.articles_controller import ArticlesController

routes = {
    r'^/home$': [SiteController, SiteController.index],
    r'^/about$': [SiteController, SiteController.about],
    r'^/test(.*)$': [TestController, TestController.test],
    r'^/action(.*)$': [TestController, TestController.action],
    r'^/hello/(.*)$': [TestController, TestController.hello],
    r'^/articles(\d+)$': [ArticlesController, ArticlesController.view],
}