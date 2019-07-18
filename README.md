<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://user-images.githubusercontent.com/51754047/61475629-3e111080-a959-11e9-8191-01b67aad8c9b.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Solar</h3>

<div align="center">

  
  [![GitHub Issues](https://img.shields.io/github/issues/bennettsean/Solar.svg)](https://github.com/bennettsean/Solar/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/bennettsean/Solar.svg)](https://github.com/bennettsean/Solar/pulls)
  

</div>

---

<p align="center"> Automating Job Submission and Analysis to a Supercomputer using Slurm
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>
Write about 1-2 paragraphs describing the purpose of your project.

The purpose of this project is to create an open source program that can hopefully aid individuals who are looking into working with Supercomputers in tandem with Atom movement analysis. This project focuses on creating an easily accessible program for scientists and researchers who are well versed in analyzing the data generated from Solar but lacking in how to exactly change a programs code for their specific needs. Solar accomplishes this by genertating the code for the submissionFile, compilationFile, logFile, and shellFile all by itself. All the user needs to do is to change the variables in the configFile.txt and Solar will automatically change the code for the user.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them.

Numpy
```
pip install numpy
```

### Installing
A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install numpy
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Running the tests <a name = "tests"></a>
Explain how to run the automated tests for this system.

### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## Usage <a name="usage"></a>
Below I am going to demonstrate how a normal run of this program would go. First you run Solar.py, then submissionFile.py. At this point in our system you'll have to check in on your jobs in the Supercomputer's queue and when you see they are all done, run compilationFile.py.

compilationFile.py does take a bit to fully do its job so if it starts to seem like its idleing on you, it's working. After all is said and done a new command line should pop up and that indicated that compilationFile.py has finished and all of the data will be in the necessary directories.



![Screenshot from 2019-07-18 13-15-40](https://user-images.githubusercontent.com/51754047/61478739-2e48fa80-a960-11e9-8fc7-8dc7963a16be.png)

![Screenshot from 2019-07-18 13-12-01](https://user-images.githubusercontent.com/51754047/61478761-3ef97080-a960-11e9-917c-00dc60ce4c85.png)

![Screenshot from 2019-07-18 13-13-07](https://user-images.githubusercontent.com/51754047/61478776-4882d880-a960-11e9-8930-6bd6985c9ae3.png)


## Deployment <a name = "deployment"></a>
Add additional notes about how to deploy this on a live system.

## Built Using <a name = "built_using"></a>
- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## Authors <a name = "authors"></a>
- [@bennettsean](https://github.com/bennettsean) 

## Acknowledgements <a name = "acknowledgement"></a>
- Mentor : Thomas Carroll @ Ursinus College
- <div>Logo made with <a href="/en/" title="Free Online Logo Maker">DesignEvo</a></div>
