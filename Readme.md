# Kottapalli Book Store

Website for kottapalli book store built using [satchmo][].

[satchmo]: http://www.satchmoproject.com/

## Setup

Clone this repository:

    $ git clone git://github.com/kottapalli-in/kstore.git
    $ cd kstore

Setup virtualenv. This installs all the required python dependencies.

    $ make venv

Setup database and load sample data:

    $ make setup

## Run

Start the dev instance by running `make`.

    $ make
    ...
    Django version 1.3.1, using settings 'kstore.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now visit <http://127.0.0.1:8000/> to see the sample site.
