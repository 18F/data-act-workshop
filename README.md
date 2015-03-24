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

### Running the Flask app using Vagrant

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Install [Vagrant](http://www.vagrantup.com/downloads.html)
3. From project root directory, run: 

         $ vagrant up

4. Once the VM is fully started and provisioned (~5 minutes), connect to it with:

        $ vagrant ssh
        
5. The project directory on your host machine is shared with the VM at `/vagrant`. Navigate there, load the virtualenv, and start the Flask application:

        $ cd /vagrant
        $ workon data-act-workshop
        $ python data.py
        
The Flask app should now be accessible from the host machine at [http://localhost:5050/](http://localhost:5050/). Because the project directory on your host machine is shared with the VM, you can use your existing tools (IDE, browser, etc.) and everything will be synced with the VM.
        
### Resources

A list of things that might be useful during the workshop.

#### Background

* [Workshop description](https://docs.google.com/a/gsa.gov/document/d/1kiEc58tfOJO3HYhE-JfGb0gjohm_sW1NEpJb-Y9Efo4/edit?userstoinvite=vladlen.zvenyach@gsa.gov&actionButton=1)
* [Glossary of Terms Used in the Federal Budget Process](http://www.gao.gov/assets/80/76911.pdf)
    * page 152 = individual pieces of Treasury Account Symbol (TAS)
* [Financial, procurement, and grant conceptual and macro models ](https://community.max.gov/pages/viewpage.action?pageId=754091525) (.gov address and MAX login required)
* [Oracle U.S. Federal Financials Implementation Guide](https://docs.oracle.com/cd/E26401_01/doc.122/e48804/toc.htm)
    * [Definition of Treasury Account Symbols (TAS)](https://docs.oracle.com/cd/E26401_01/doc.122/e48804/T340593T340601.htm)
* [Business Event Type Code (BETC) Fact Sheet](http://fms.treas.gov/cars/factsheet_betc.html)
    * TAS + BETC classifies a transactions against a Treasury fund balance
    * [Spreadsheet of all BETC](http://fms.treas.gov/cars/BETC-factsheet-03-01-12.xls)
* Object Class
    * [Defined in OMB A-11](https://www.whitehouse.gov/sites/default/files/omb/assets/a11_current_year/s83.pdf)

**General Ledger Links. May not be relevant for workshop.**

* [GTAS attribute definitions and bulk file layout](http://www.fiscal.treasury.gov/fsservices/gov/acctg/gtas/bulk_file.htm)
* [USSGL Accounts and Definitions (PDF)](http://tfm.fiscal.treasury.gov/v1/supplements/ussgl/ussgl_part_1/sec2/sec2_acctdef_2014.pdf)
* [PwC GL Taxonomy Docs](https://drive.google.com/drive/#folders/0B5HeQa_YQ6-VfngwcGFwRDg5WlpiY2R1Vk1iOHZzN3gzVFV3YlhxS2JnTllZY2lqbnA2Z2c/0B4JtVmWTTdQEfnNBaWRIeFFMTi12cUFiRENLM2ZBVXVBWFplUnNNbU9VWFU0NUhwc0tKczQ)
* Report on Budget Execution and Budgetary Resources (SF-133)
    * [Defined in OMB A-11 (PDF)](https://www.whitehouse.gov/sites/default/files/omb/assets/a11_current_year/s130.pdf)
    * [Agency SF-133s (PDF & XML)](https://max.omb.gov/maxportal/document/SF133/Budget/FY%202014%20-%20SF%20133%20Reports%20on%20Budget%20Execution%20and%20Budgetary%20Resources.html)
    * USSGL to SF-133 crosswalk
        * [USSGL to SF-133 crosswalk (XLS)](http://www.google.com/url?q=http%3A%2F%2Ftfm.fiscal.treasury.gov%2Fcontent%2Fdam%2Ftfm%2Fv1%2Fsupplements%2Fussgl%2Fussgl_part_1%2Fsec5%2Fsec5_sf133_2014.xls&sa=D&sntz=1&usg=AFQjCNFURjTQLus2j9GbpxL8Wns5Ha9x2Q)
        * [SF-133/USSGL/DATA Act crosswalk](https://drive.google.com/open?id=19mkvYQUa_ICIcGtK59_U62EEqSysAj8K5pCK6Yx3Vek&authuser=0)
    * [Concatenated quarterly SF-133 reports](https://github.com/18F/data-act-sf133)
        * [SF-133 fields related to DATA Act](https://drive.google.com/open?id=0B4JtVmWTTdQER29pc2ltQlFLelk&authuser=0)
        * [iPython notebook](http://nbviewer.ipython.org/github/18F/data-act-sf133/blob/master/Budget%20Execution.ipynb)

#### Tech Guides

* [Protocol Buffers docs](https://developers.google.com/protocol-buffers/)
* [Flask docs](http://flask.pocoo.org/)
* [18F Cloud Foundry docs](https://docs.cf.18f.us/)
* [Workshop app on Cloud Foundry](http://data.cf.18f.us/)
* [What Can You Do With PostgreSQL and JSON?](http://clarkdave.net/2013/06/what-can-you-do-with-postgresql-and-json/)
