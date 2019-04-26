import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                Column('id', Integer, primary_key=True),
                                Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                Column('employee_id', Integer, ForeignKey('employee.id'))
                                )


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name


class Celebs(Model):
    __tablename__ = 'Celebs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    movies_id = Column(Integer, nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")


class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class CelebsNews(Model):
    __tablename__ = 'celebs_news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    description = Column(String(500), nullable=False)


class CelebsPopularity(Model):
    __tablename__ = 'celebs_popularity'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)


class Movies(Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    director = Column(String(50), nullable=False)
    stars = Column(String(50), nullable=False)


class MoiveGenre(Model):
    __tablename__ = 'movie_genre'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)
    series = Column(String(50), nullable=False)


class Series(Model):
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer,  nullable=False)
    name = Column(String(50), nullable=False)
    season = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)


class Event(Model):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    event = Column(String(50), nullable=False)
    celebs_name = Column(String(50), nullable=False)
    celebs_id = Column(Integer,  nullable=False)


class Oscars(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)


class GoldenGlobes(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)


class Photos(Model):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    photos_name = Column(String(50), nullable=False)
    photots_year = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    people = Column(String(50), ForeignKey(Celebs.name), nullable=False)
