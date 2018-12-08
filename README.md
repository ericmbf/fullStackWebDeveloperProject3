# Projetct 3 FullStackDevelopment Udacity
This repository is used to implement the third project from Udacity Full Stack Development nanodegree. In the project it is needed response 3 questions using sql query.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
1- A good browser

2- A terminal

3- Vagrant

4- Virtualbox

```
## Steps
```
* Init vagrant using "vagrant up"
* Do ssh connection with virtual machine using "vagrant ssh"
* You need exec this query on psql to create the views necessary to program works.
 * "create view get_error as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req 
    from log where log.status like '%404%' group by date;"
 * "create view get_all as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req 
    from log group by date;"
* Exec the irt.py program exec the command line: "python irt.py"
```

## How to Contribute

If would like to contribuite com this code, please fork the repository.

```sh
$ git clone https://github.com/ericmbf/project3FullStackDevelopment.git
```

## License

The contents of this repository are covered under the [MIT License](LICENSE).