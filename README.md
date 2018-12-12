# Projetct 3 FullStackDevelopment Udacity
This repository is used to implement the third project from Udacity Full Stack Development nanodegree. In the project it is needed response 3 questions using sql query.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. It was used the sql "nwsdata.sql" file to create the database called "news".

### Prerequisites

What things do you need use the program

```
1- A good browser

2- A terminal

3- Vagrant

4- Virtualbox

5- Download the vagrant VM with all the files needed to init and enter into VM.

6- Install psycopg2 library python inside Vagrant VM to do postgres database operations. 
```
[Link to Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
## Steps
```
* Open the file above and extract all.
* Search for the file "Vagrantfile" and open the terminal on directory from file.
* You need to init the VM using "vagrant up" where the "Vagrantfile" is localized.
* Do ssh connection with virtual machine using "vagrant ssh" to enter inside the VM after started the VM.
* Type "psql news" on terminal to open the "news" table on PostgreSQL. 
* Exec the query's on below this steps.
* Clone this repository inside VM.
* Exec the irt.py after all to using the command line: "python irt.py" and wait some seconds for the result.
```

## Views
```
    create view get_error as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req from log where log.status like '%404%' group by date;

    create view get_all as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req from log group by date;"
```

## How to Contribute

If would like to contribuite with this code, please fork the repository.

```sh
$ git clone https://github.com/ericmbf/project3FullStackDevelopment.git
```
