<!-- ABOUT THE PROJECT -->
## About The Project

This project is dedicated for those that hate the whole "networking bullshit" disease that is linkedin. Most engineering students like me cannot stand the whole process of looking for a job which solely consists of kissing ass to recruiters in the hopes they let you skip the OAs and go straight to on-sites or virtual interviews. So I wanted to create a little family of webscrapers for linkedin that all have a different roles and some customizability for what you want. The first base webscraper is used to search through all job pages for a specified role and find all the technical recruiters of that specific company for you to reach out to. The other webscrapers will essentially act as auto-message bots that read from a .csv file containing all the recruiters/ppl you want to contact without having to do the labor yourself.

Here's why:
* The whole idea of "networking" is a morally decrepit maxim that us engineering students are obligated to equally participate in, but NO MORE!
* You shouldn't be writing the same recruiter messages over and over by hand, automate it
* Automation is ALWAYS superior to doing something manually



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* BeautifulSoup
* Selenium
* Pandas

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

A few python libraries will need to be installed and updated version of python 

### Prerequisites

* Python3
  ```sh
  # windows users:
  Download py3 executable and run
  # Linux users:
  You know what to do
  # mac users:
  echo "Quit using this machine"
  ```
* BeautifulSoup
  ```sh
  pip install beautifulsoup4
  pip install lxml
  pip install requests
  ```
* Selenium
  ```sh
  pip install selenium
  pip install webdriver-manager
  ```


### Installation

_Steps before running python script_

1. Clone the repo
   ```sh
   git clone https://github.com/gillespie-alex/linkedin_web_scrapers.git
   ```
   
2. Install python then have access to pip (python package installer) and run pre-reqs in order

3. Open python file with
   ```sh
   # DO NOT USE VISUAL STUDIO CODE EVER AGAIN
   vim linkedinscraper.py
   ```
   
4. Enter your linkedin credentials in .py file
   ```py
   email = 'eg@gmail.com'
   password = 'passwd'

   position = 'desired position'
   local = 'your locality'
   ```
   
5. Lauch python file with
   ```sh
   python linkedinscraper.py
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
--> 

