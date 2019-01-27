# Website for UDES

### Tech
* TODO

### Production Server
* Build Python environment and install dependencies as explained [here](https://bitbucket.org/mania_dev/flask-boilerplate)
* In ```core/static/``` run
```yarn install```
* Change values in the following files
    * ```instance/config.py```
    * ```run.sh```
* ```flask run``` may need to be passed a 0 IP value
* Open terminal and run
```sh run.sh```
* Hit the URL

### Debugging
* Check if the following were created
    * core/static/css/styles.css
    * core/static/gen/packed.css
    * core/static/gen/packed.js

### Known Issues
* /bulma/sass/layout/footer.sass has .footer padding value hard set. Change to $footer-padding to make use of sass variables set in styles.scss

Note: The compressed packed.* files are only created if the ASSETS_DEBUG value is set to False