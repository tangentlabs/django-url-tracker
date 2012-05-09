#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in oscar.__init__.py
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

setup(
    name = "django-url-tracker",
    version = '0.1.1',
    url = "https://github.com/tangentlabs/django-url-tracker",
    author = "Sebastian Vetter",
    author_email = "sebastian.vetter@tangentone.com.au",
    description = ("A little app that trackes URL changes in a database table "
                  "to provide HTTP 301 & 410 on request."),
    long_description = open('README.rst').read(),
    license = "BSD",
    packages = find_packages(exclude=["docs*", "tests*"]),
    include_package_data = True,
    install_requires=[
        'django>=1.3.1',
        'South>=0.7.3',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    keywords = "seo, django, framework",
)


