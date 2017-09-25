# **Release Procedure as of 1.0** 

### **Introduction / summary**
The current release procedure for todo application involves a combination of an automated release script and a few manual steps. Our goal is to ensure that the Future versions will automate more of the process, if not all.

### **Release Procedure**
**This is the standard release procedure for releasing todo app.**

We haven't really followed the proper maintenance branch approach, thus including all affiliated packages of the MVP on a single branch (master) but prospective better releases will see us adopt better practices as far as branching is concerned. 

Being the first version (initial), we have not included the "what's new section" that would show the major upgrades since the previous version was released. From the feedback that we shall be getting in the next few months, we shall include;
 
> *issues*
> *PR's*
> *and the contributors to those releases that shall be versions semantically*

On major releases, we will be sure to include any new contributors on the todo app but might not necessarily do that on minor bug fix releases.

Note: You don't need to set up a clean environment to build the release since it has no previous version. For more on setting up virtual environments, see Python virtual environments. 

For this release, you will first do the main installations; follow the steps below

Installation

Clone the GitHub repo and cd into the folder and install a virtual environment:

```
$ git clone https://github.com/SProjects/ops-todo.git'

$ virtualenv venv

Activate the virtual environment

$ venv/bin/activate

Install all app requirements

$ pip install -r requirements.txt Create the database and run migrations
```

There are Options for the db, you could use sqlite (which is the default) or postgresql

>postgresql
```
$ createdb todo_db (for staging environment)

$ createdb test-todo_db (for testing environment)

$ python manage.py db init

$ python manage.py db migrate

$ python manage.py db upgrade
```
then; 
to ensure all **requirements / dependancies** are installed, run 
```
$ pip install -r requirements.txt 
```
### **Build management**

Make sure that the continuous integration services (CircleCi for our case) are passing for master app branch you’re going to follow. You may also want to locally run the tests (with remote data on to ensure all the tests actually run), and make sure you have additional scripts which help in bump versioning and deploying the application to heroku

We are using circleC1 workflow consisting of build, test, bump_versioning and deployment. Not that bumping isn't dependent on any workflow during the build.]

### **Beta Releases**
For the future releases, the following will guide the next version successfully;

Proper branching for bugfixes


> Proper branching for major releases

**steps**
- branching off master to develop then creating the feature branch.
- doing the versioning (committing along with the tagging).

> Versioning the release
- semvar
- currently on Alpha v1.0.0
- next will be Alpha v1.0.1-10 (for all patches and bugfixes)
- major release will be Beta v1.0.0