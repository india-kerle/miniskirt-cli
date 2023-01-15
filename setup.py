from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'mini_skirt',
    version = '0.0.0',
    author = 'India Kerle',
    author_email = 'india.kerle@sciencespo.fr',
    license = 'MIT',
    description = 'should you wear a miniskirt',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = '',
    py_modules = ['miniskirt', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        miniskirt=miniskirt:cli
    '''
)