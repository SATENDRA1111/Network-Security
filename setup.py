from setuptools import setup,find_packages

''' setup.py file is essensial part of packgining and distributing python preject
it is used by setuptools to difine configration of your project. such as its difine metadatas,dependencies and more
'''

requirements_lst:list[str]=[]
def get_requirements()-> list[str]:
    '''this function will returen list of requirements'''
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            ##process each lines
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and .e
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
            
    except FileNotFoundError:
        print("file not found")
    

    return requirements_lst

print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Satenera Dwivedi',
    author_email='satendradwivedi161@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
    