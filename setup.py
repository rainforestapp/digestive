import sys
from setuptools import setup, find_packages

requires = [
    'pygithub',
    'cssselect',
    'lxml',
    'premailer',
    'pygithub3',
    'requests',
    'wsgiref'
]


setup(
    name='digestive',
    version='0.1',
    description='Templatable Github digest emails',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Monitoring',
    ],
    author='Rainforest QA',
    author_email='team@rainforestqa.com',
    url='https://github.com/rainforestapp/digestive',
    keywords='github email',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': [ 'digestive=digestive:main' ],
    },
)

