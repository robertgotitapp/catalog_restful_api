from setuptools import setup, find_packages

setup(name="catalog_restful_api",
      packages=find_packages(),
      install_requires=[
          'flask',
          'Flask-RESTful',
          'Flask-JWT',
          'Flask-SQLAlchemy',
          'Marshmallow==3.0.0rc6',
          'uwsgi',
          'mysql-connector',
      ],
      extras_require={
        'test': [
            'pytest',
            'coverage',
            'pytest-cov'
        ],
    })