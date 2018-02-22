# Thai Tokenizer

A Recurrent Neural Network which separates thai sentences into individual words. Built with Keras using Tensorflow as the back end and hosted on [Heroku](https://thai-tokenizer.herokuapp.com/) using Gunicorn/Flask.  The Jupyter Notebook where the model was developed can be found [here](https://github.com/LazyElephant/Machine-Learning-Notebooks/blob/master/Day%206%20-%20Model%20for%20Thai%20text%20tokenization.ipynb).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The only requirement to use this server is Python 3.6.  I personally like to use [Anaconda](https://conda.io/docs/user-guide/install/download.html).

### Installing

Clone this repository and install required packages

``` bash
$ git clone https://github.com/LazyElephant/Thai-Tokenizer.git
$ cd Thai-Tokenizer
$ pip install -r requirements.txt
```

Start the local flask development server.

``` bash
$ export FLASK_APP=server.py && python -m flask run
```

## Built With

* [Flask](http://flask.pocoo.org/)
* [Gunicorn](http://gunicorn.org/)
* [Python](https://www.python.org/)
* [Keras](https://keras.io/)
* [Tensorflow](https://www.tensorflow.org/)
* [Heroku](https://www.heroku.com/)
* [Thai look-alike font](http://www.weygandt.de/aw_siam/)

## Authors

* **Tim Schmidt** - *Initial work* - [LazyElephant](https://github.com/LazyElephant)
