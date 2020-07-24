import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="kladama-api", # Replace with your own username
    version="1.0.4",
    author="Plexilar",
    author_email="hdkrus@gmail.com",
    description="Kladama API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plexilar/kladama-api-python",
    packages=setuptools.find_packages(include=['kladama', 'kladama.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='kladama api',
    install_requires=[
        'jsonlib-python3',
        'requests'
    ],
    python_requires='>=3.6',
)
