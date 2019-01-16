from setuptools import setup, find_packages

setup(
    name="gerby",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "PyPDF2",
        "Markdown",
        "mdx_bleach ",
        "python-markdown-math ",
        "validators ",
        "flask ",
        "peewee ",
        "flask_profiler ",
        "feedparser "])

