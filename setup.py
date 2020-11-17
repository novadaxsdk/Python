import setuptools

print(setuptools.find_packages())

setuptools.setup(
    name="novadax",
    version="1.1.0",
    author="NovaDAX",
    author_email="support@novadax.com",
    description="NovaDAX API SDK",
    url="https://doc.novadax.com/",
    packages=["novadax", "novadax.exception", "novadax.kernel"],
    install_requires=['requests']
)