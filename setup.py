from setuptools import setup, find_packages

setup(name="catalog_restful_api",
      packages=find_packages(),
      install_requires=[
          'Flask',
          'Flask-RESTful',
          'Flask-JWT',
          'Flask-SQLAlchemy',
          'flask-cors',
          'Marshmallow==3.0.0rc6',
          'uwsgi',
          'mysql-connector',
          'virtualenv',
          'pytest',
          'coverage',
          'pytest-cov'
      ],
      extras_require={
    })