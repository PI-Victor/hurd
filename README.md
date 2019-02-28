Pinner
---
Unifies microservices under a single platform version for CI/CD platform deployment.  
This tool aims to fix the issue with managing microservices within the CI/CD pipeline,
it will aid in the deployment of microservices under a single platform.  

#### Workflow
Create a new git repository, it is recommanded you give it the name of your platform.  
We are going to work with an example created specifically for this tool.  
Please see github.com/codeflavor/platform-test.  
Inside the new repo, create a `config.yaml` file. This file will define a basic config
for your microservices.  
Each component, in this case each microservice, is specified as follows:   
```yaml
---
name: platform-test
components:
  - alias: test1
    url: git@github.com:codeflavor/test1.git
  - alias: test2
    url: git@github.com:codeflavor/test2.git
  - alias: test3
    url: git@github.com:codeflavor/test3.git
```
`name` - the name of the platform.  
`components` - all of the components that the platform contains.  
This does not only encompass microservices, but everything the platform is comprised of.
 e.g.: Microservices, Database schema, Swagger/OpenAPI schema, etc.  

This config must have a name for the component and point to the repository URL.  



#### Installing and deps
This project depends on python 3.7+ install
[python virtualenv](https://virtualenv.pypa.io/en/latest/).  

Prerequisites:

> python 3.7   
libgit2,  libgit2-glib - needed for macbook and fedora.

```bash
$ virtualenv -p python3 .venv
....
# activate the virtualenv

source .venv/bin/activate
```

Now you can install the application

```bash
$: python3.7 setup.py install
```