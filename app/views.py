from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee, Department, Function, EmployeeHistory, Benefit, Celebs, Movies, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    # base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department': QuerySelectField('Department',
                                                             query_factory=department_query,
                                                             widget=Select2Widget(extra_classes="readonly"))}

    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']


class CelebsView(ModelView):
    datamodel = SQLAInterface(Celebs)
    list_columns = ['id', 'name', 'link', 'menu_category_id']


class MovieView(ModelView):
    datamodel = SQLAInterface(Movies)
    list_columns = ['id', 'name']


class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']


class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']


class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)


class MoviesPageView(BaseView):
    default_view = 'in_theaters'

    @expose('/in_theaters/')
    def in_theaters(self):
        param1 = 'In Theaters'
        self.update_redirect()
        return self.render_template('movie.html', param1=param1)

    @expose('/top_rated_movie/')
    def top_rated_movie(self):
        param1 = 'Top Rated Movie'
        self.update_redirect()
        return self.render_template('movie.html', param1=param1)

    @expose('/oscar_winner/')
    def oscar_winner(self):
        param1 = 'Oscar Winner'
        self.update_redirect()
        return self.render_template('movie.html', param1=param1)


class CelebsPageView(BaseView):
    default_view = 'born_today'

    @expose('/born_today/')
    def born_today(self):
        param1 = 'Born Today'
        self.update_redirect()
        return self.render_template('celebs.html', param1=param1)

    @expose('/latest_posters/')
    def latest_posters(self):
        param1 = 'Latest Posters'
        self.update_redirect()
        return self.render_template('celebs.html', param1=param1)

    @expose('/celebrity_news/')
    def celebrity_news(self):
        param1 = 'Celebrity News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
    
class ShowTimePageView(BaseView):
    default_view = 'opening_this_week'

    @expose('/opening_this_week/')
    def (self):
        param1 = 'Opening This Week'
        self.update_redirect()
        return self.render_template('moive.html', param1=param1)

    @expose('/now_playing/')
    def latest_posters(self):
        param1 = 'Now Playing'
        self.update_redirect()
        return self.render_template('moive.html', param1=param1)

    @expose('/comeing_soon/')
    def (self):
        param1 = 'Comeing Soon'
        self.update_redirect()
        return self.render_template('movie.html', param1=param1)


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")
appbuilder.add_view(MoviesPageView, 'In Theaters', category="Movie")
appbuilder.add_link("Top Rated Movie", href="/moviepageview/top_rated_movie/", category="Movie")
appbuilder.add_link("Oscar Winner", href="/moviepageview/oscar_winner/", category="Movie")
appbuilder.add_view(CelebsPageView, 'Born Today', category="Celebs")
appbuilder.add_link("Latest Posters ", href="/celebspageview/latest_posters/", category="Celebs")
appbuilder.add_link("Celebrity News", href="/celebspageview/celebrity_news/", category="Celebs")
appbuilder.add_view(ShowTimePageView, 'Opening This Week', category="")
appbuilder.add_link("Now Playing", href="/ShowTimePageView/now_playing/", category="")
appbuilder.add_link("Comeing Soon", href="/ShowTimePageViewShowTimePageView/comeing_soon/", category="")

""" Custom Views """
appbuilder.add_view(CelebsView, "Celebs", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MovieView, "Movies", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
