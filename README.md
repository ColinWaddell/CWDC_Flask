Hello
=====
I've decided to port my site from wordpress to my own little [Flask](http://flask.pocoo.org/) cms.

The idea is anything I want to edit or publish can be done through the ```content/``` directory. For example. The file ```content/projects.md``` would be served up at ```colinwaddell.com/projects```. The look of the site is handled via ```templates/```.

Also bundled into this project is a ```Gruntfile.js``` which will allow you to serve the site using [BrowserSync](https://www.browsersync.io/). CSS is generated via sass which this ```Gruntfile.js``` also takes care of.

Installation
============
Grab a copy:
```
git clone git@github.com:ColinWaddell/CWDC_Flask.git
cd CWDC_Flask
```

Setup a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv):
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Install all the [required tools](https://www.npmjs.com/):
```
npm install
```

You'll also need to create a file called ```./key.py``` and put in it:
```
SECRET_KEY = 'something_random'
```
**Be sure to avoid tracking this file in git.**

Build all the css (this will be handled automatically when using the ```grunt``` command on its own):
```
grunt sass
```

Now you can set it running! This will open a browser, sometimes I need to refresh this when it first loads to get it to sync up properly.
```
grunt
```