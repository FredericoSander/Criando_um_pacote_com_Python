from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="data_analisys",
    version="0.0.2",
    author="Frederico S N Cota",
    author_email="sanderfn@hotmail.com",
    description="Geração de estatísticas do arquivos CSV",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FredericoSander/Criando_um_pacote_com_Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)