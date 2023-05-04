from setuptools import setup, find_packages

setup(
    name="qbidolet_02_mai",
    version="0.1.0",
    packages=find_packages(),
    install_require=[
        # dépendances de votre package
    ],
    author="Quentin BIDOLET",
    author_email="quentin.bidolet@gmail.com",
    description="Une brève description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)