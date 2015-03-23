## DATA Act Agile Workshop - March 25th-26th

This repo contains a basic python/flask project with protofbuf support.

To compile protobuf messages into python classes, see [the installation instructions on the protobuf repo](https://github.com/google/protobuf)

The current working protobuf messages are in [this repo](https://github.com/18F/data-act-schemas/).

### Running the Flask App Locally

1. Install PostgreSQL 9.4
2. Install Python 2.7
3. Install virtualenv
4. Clone the project repo and cd into it:

        $ git clone git@github.com:18F/data-act-workshop.git
        $ cd data-act-workshop

5. Create a virtual environment:

        $ mkdir env
        $ virtualenv ./env

6. Activate the virtual environment. After the virtual environment is activated, you should see `(env)` on your command prompt.

        $ source env/bin/activate

7. Install the required Python packages:

        $ pip install -r requirements.txt

8. Start the Flask application:

        $ python data.py

The Flask application should now be running at  [http://localhost:5000/](http://localhost:5000/).
