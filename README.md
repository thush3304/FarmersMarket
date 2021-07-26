# Farmers Market 
## Contents


## Introduction

### Aims
The aims for this project are:
> To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

For me this means:
1. Utilise CRUD within the program created by me.
2. Use JIRA to develop a methodology.
3. Create an Entity Relationship Database (has to have a one-to-many relationship)
4. Assess all risks and create a risk assessment detailing this.
5. Build tests that will test the functionality of the application.
6. Fully integrated with GitHub.
7. Use Flask for front-end on website production.

### My Idea
I have decided to create an application for farmers which will enable them to both sell their goods to customers as well as lend tools to other farmers. Other farmers can then rent out tools from others as well as put up stock for any new goods.

The CRUD for this application is outlined below:

#### Create:
* Farmers details
* Goods stock 
  * Vegetables
  * Fruits
  * Meat
  * Dairy
* Tools
  * Vehicles
  * Power tools
#### Read:
* Available produce to purchase
* Tools to rent
#### Update:
* Farmers details
* Stock amount
#### Delete:
* Farmers details
* Goods
* Tools

## Architecture:
### Risk Assessment:
Below I have created a risk assessment which outlines the various risks with the application development and the application itself alongside the potential fixes. As shown there have been additions to the list of risks, this is because whilst programming the program the potential risks of the system became more apparent, hence they had to be addressed.
![image](https://user-images.githubusercontent.com/86304577/126946228-881e7e60-afdd-4c39-9fb3-8bbd785b6b08.png)

### JIRA BOARD:
Below is how I have documented my progress of the project using JIRA. This application was used as it was the one that I am well-versed in and it is fairly easy to use.

![image](https://user-images.githubusercontent.com/86304577/126947371-e63bfa58-f4db-4564-8813-de1c8f23b174.png)This board will get updated and the full board can be accessed at: https://thushithqa.atlassian.net/jira/software/projects/FM/boards/2/roadmap

### Entity Relationship Diagram:
Below is the current Entity Relationship Diagram I have developed. This will get developed as more sections are added onto the project, however for now as shown it satisfies the aim of a one-to-many relationship database. 

![image](https://user-images.githubusercontent.com/86304577/125354099-4db26c80-e35b-11eb-9967-cdc37264dc60.png)

A one-to-many relationship was used for this application solely due to the fact that this is what is required for application. 
The above was updated to:
![image](https://user-images.githubusercontent.com/86304577/126941303-e969974b-0a0a-4461-8fe9-dd5df8240b2e.png)
This is because the model above is more complicated than what is required for the task and as both tables list what the farmers are selling the need for two separate tables is redundant. This eases the work load for me as well as satisfies the condition on a one to many relationship as one farmer can have several crops to sell etc. This updated model further shows the coherence between both tables rather than splitting the information across two tables presenting in one table makes the work also easier for me to implement. The farmers table holds all personal details including their name, age and farm's name, whilst the goods table holds all physical things that can be sold by

### Analysis of Testing:
The forms of testing used are Unit testing and Integration Testing. For each section of the CRUD development tests were created so that the output can be tested and verified with the test cases. Whilst going through the testing process for both create and update, the data added were not being added under their respective columns instead adding them in the row as a new entry. This would have ultimately defeated the point of the one-to-many relationship of my database structure, as of now the formating works perfectly after debugging and sorting out the issues.
![image](https://user-images.githubusercontent.com/86304577/126945355-a82374a4-6873-4c75-ad3d-e643a9d2de31.png)

### Continuous Integration:
![image](https://user-images.githubusercontent.com/86304577/126948030-cb0cae6d-b8c8-43fc-804f-0d1ea5b0ef9a.png)
The above shows the process for the continuous integration that has been implemented for this project. This is utilised to give faster production and deployment as well as automated testing without having to run coverage or unit tests manually. Using the reports attained the overall project can be changed/fixed to further suit the aims.

### Development:
The following was entered into Jenkins for integrated testing:
#!/bin/bash

sudo apt install chromium-chromedriver -y
sudo apt-get install python3-venv 

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt 

pytest tests/testunit.py --cov=. --disable-warnings

if [ -f pytest-result ] && [ $(cat pytest-result) == 'FAIL' ]; 
	then echo "TESTING FAILED - MARKING BUILD AS FAILED"; exit 1;
fi;

From which the following coverage was attained for the main files:
![image](https://user-images.githubusercontent.com/86304577/126948984-388d09a9-6411-4746-82c3-aef1c9ce4b12.png)
![image](https://user-images.githubusercontent.com/86304577/126949078-87ad7e9e-0c4d-4a8c-b13a-a78413c5f37f.png)
The total coverage was only 40% however this was due to the fact that the create.py file was not being tested by my unit tests however the other files tested were fully functional to a certain extent.

### Front End:
![image](https://user-images.githubusercontent.com/86304577/126949837-3651fb45-d0de-4232-a5e6-37987f3c1522.png)
The above image is what the user is presented with as they enter the site, this is the homepage which shows the database and presents all necessary data. It also has a navigation bar at the top to access the create new section. The options to both update and delete the rows are also on this page.
![image](https://user-images.githubusercontent.com/86304577/126950003-53bb4e7d-ce77-4378-ac0f-84c56436183c.png)
These are the buttons which enable for the update and deletion of the row.
Below is an example of updating the total number of celery in row 2.
![image](https://user-images.githubusercontent.com/86304577/126950376-c3af1a1b-3829-4c6a-b645-4a5315e28040.png)
Notice how all values are the same except for the number of celery which has increased, this is because that is the only value we wish to change.
![image](https://user-images.githubusercontent.com/86304577/126950621-4e76d382-2b12-4e79-b022-eeb05f904c6f.png)
As shown the table has been updated.
The create section looks like this:
![image](https://user-images.githubusercontent.com/86304577/126950787-1f4a5ee2-a3e5-4712-b522-fb0bf1b0194b.png)

## Footer:
### Further Improvements:
* Add in a login page for added security
* Prevent failing of create and update, these had several problems and worked at times as shown above.
* Create a more appealing template using HTML that is easier to navigate and read
* Separate out the navbar

### Author
Thushith Premadas

### Acknowledgements

Oliver Nichols
Ryan Wright
QA Community - for providing good tutorial on using Jenkins

### Versions
26/07/2021 - v1.0.0.0







