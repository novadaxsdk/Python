from setuptools import setup, find_packages

setup(
    name="novadax",
    version="1.1.2",
    author="NovaDAX",
    author_email="support@novadax.com",
    description="NovaDAX API SDK",
    url="https://doc.novadax.com/",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'requests>=2,<3',
        'python-socketio[client]'
    ]
)
