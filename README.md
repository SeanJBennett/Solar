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

<p align="center"> Automating Job Submission and Analysis to a Supercomputer in Python using Slurm
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>

Solar is a program written in Python that automatically generates more Python code from a simple configuration text file and automatically submits jobs to a Supercomputer's queuing system using Slurm. This makes Solar very useful to those who need to submit many jobs to a Supercomputer and those with limited coding experience. Solar makes use of Slurm for job submissions to our Supercomputer but can be easily adapted to your choice of communication system.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

- Numpy
- Slurm - or your choice of Job Submission System


### Installing

```
pip install numpy
```

```
https://www.schedmd.com/downloads.php
```


## Usage <a name="usage"></a>
Solar, as stated above, automaically generates code and automatically sends jobs to a Supercomputer. Additionally, Solar creates and curates log files, results files and raw data that is taken right from the Supercomputer (see Solar Examples).

- Step 1 and 2

![Screenshot from 2019-07-18 13-15-40](https://user-images.githubusercontent.com/51754047/61478739-2e48fa80-a960-11e9-8fc7-8dc7963a16be.png)

- Step 2 in progress

![Screenshot from 2019-07-18 13-12-01](https://user-images.githubusercontent.com/51754047/61478761-3ef97080-a960-11e9-917c-00dc60ce4c85.png)

- Step 3 in progress

![Screenshot from 2019-07-18 13-13-07](https://user-images.githubusercontent.com/51754047/61478776-4882d880-a960-11e9-8930-6bd6985c9ae3.png)


## Deployment <a name = "deployment"></a>

The configuration file ultimately dictates what Solar does. Any changes to the configuration file will automatically appear in Solar and the other generated code upon running. How I've set up Solar to work with the configuration file is that the position/line number of the paramaters does matter but it can be easily changed to be fluid.

## Built Using <a name = "built_using"></a>
- [Slurm](https://www.schedmd.com/) - Communicating with the Supercomputer
- [Python](https://www.python.org/) - Coding Language

## Authors <a name = "authors"></a>
- [Sean Bennett](https://github.com/bennettsean) 

## Acknowledgements <a name = "acknowledgement"></a>
- Mentor : [Thomas Carroll @ Ursinus College](https://www.ursinus.edu/live/profiles/186-thomas-carroll)
- <div>Logo made with <a href="/en/" title="Free Online Logo Maker">DesignEvo</a></div>
