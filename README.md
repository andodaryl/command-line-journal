# Command Line Journal

## Disclaimer
The stories, people, brands and products in this software development project are fictitious and any resemblance to real life occurrence is by pure coincidence. The developer of this project, as part of an academic portfolio, referred to and used various open source materials available online to create an interactive brochure website, all of which are credited at the end.

## Project Overview
Grey Operations is a sole propiertorship which offers productivity software solutions.

This backened development project is an MVP for a greater scope related to the development of automated processing of data stored in spreadsheets.

The current objective is to create a command line interface application for journal entry management.

## Stakeholder Expectations

### Business, Research and Development Case
Assess viability of various technologies such as Heroku and Google Sheets API.

### Target Audience
This is an internal project for research and development. 
Current scope of features are suitable for software hobbyists that wish to use the terminal for logging text data for later processing via Google Sheets.

### User Experience

Product use-case outlined in terms of user needs.

As a user of this web application I want to be able to:

1. Create, retrieve, update and delete journal entries via terminal.
2. Store data in Google Drive for further processing.
3. Save data even after exiting application.

## Project Management

Managed using Prince2 methodology in para-sequential stages where features are developed in phases during which the project can terminte while delivering a usable and meaningful set of product features. Stage X commences when all stages are completed or terminated early.

Stage 1
* User Input System
* Data Manipulation System
* Save System

Stage 2
* User Input Feedback
* Backup System
* New User Input: Custom ID/Timestamp with Error Handling

Stage 3
* New Front End Design
* More Data Types For Journal Entries

Stage X
* Final testing and bug fixing

## Design

### Code Logic Diagram

[Drawio](https://www.diagrams.net/) was chosen for the wireframing environment as it offers desired functions for free and runs within the chosen coding environment (Gitpod) using an [unofficial plugin](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) for simplified access.

### Front End

A template is used to display a terminal window for user input.
Currently this is the visual design choice to focus efforts on back-end development.

## Development Log

### Features

#### Implemented

* Data Manipulation System 
* Save System

#### Backlog

* User Input System
* User Input Feedback

### Bugs

#### Fixed  
* Import Error caused by `pynput` module for Python - fixed by using `keyboard` module according to this [forum discussion](https://unix.stackexchange.com/questions/427345/keyboard-monitoring-without-display). Screenshot [here](./dev/media/pynput_error.png).

#### Backlog
* * Import Error caused by `keyboard` module for Python - to be fixed by using `Python-evdev` module as an alternative. Screenshot [here](./dev/media/keyboard_error.png).

### Testing

#### Validator Testing

#### User Experience Testing

#### Manual Testing

## Deployment

With the help of this [tutorial](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true), the website was deployed to Heroku using the following steps:
0. Enter and run `pip3 freeze > requirements.txt` to record app dependencies.
1. After signing up / logging in to Heroku, select the `New` button.
2. Select `Create New App` in the drop-down menu that appears.
3. Enter a unique name for your application.
4. Select a region.
5. Select the `Create App` button.
6. In the menu that appears at the top of the page, select the `Settings` button.
7. Go to the `Config Vars` section and select the `Reveal Config Vars` button.
8. For `Key` enter the word _port_, for `Value` enter the number _8000_, and then select the `Add` button.
9. Go to the `Buildpack` section and select the `Add Buildpack` button.
10. Select `python` in the drop-down menu that appears.
11. Select the `Add Buildpack` button again and select `node.js` in the drop-down menu that appears.

Note _Python_ must be added to the buildpack before _Node.js_

12. In the menu that appears at the top of the page, select the `Deploy` button.
13. Go to the `Deployment method` section and select the `Github` button to deploy via Github.
14. Sign in to Github if required and authorize Heroku to connect to Github.
15. Go to the `Connect to Github` section, enter the repository name, and select the `Search` button.
16. Select the `Connect` button that appears beside the desired repository.
17. Go to the `Automatic deploys` section, select the appropriate branch, and select the `Enable Automatic Deploys` button.
18. For manual deployment, go to the `Manual deploy` section, select the appropriate branch, and select the `Deploy Branch` button.
19. Carry out Step 18 to deploy the app immediately or Step 17 to deploy the app when changes are 'pushed'.

The live page is available [here](https://command-line-journal.herokuapp.com/).

## Forking Github Repos

According to [official Github documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo), this repo can be forked using the following steps:
1. After logging in, navigate to the target Github repo.
2. Select the "Fork" button located in top-right area of the page.
3. Select target location for the forked repo.

## Cloning Forked Repo via HTTPS

Additionally, you can download a local copy of the forked repo using the following steps:
1. After logging in to Github, navigate to the desired forked repo.
2. Select the "Code" button.
3. Copy the URL link below "Clone with HTTPS".
4. In a terminal with "GIT" installed, navigate to your target directory.
5. Using the `git clone` command, paste in the URL and press enter:
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPO 
\> Cloning into `YOUR-REPO`...
\> remote: Counting objects: 10, done.
\> remote: Compressing objects: 100% (8/8), done.
\> remove: Total 10 (delta 1), reused 10 (delta 1)
\> Unpacking objects: 100% (10/10), done.
```

## Credits

Maintaining competence requires continuous learning from and reflection upon the work of others. It is important to give credit and acknowledgement not only to recognise time and effort expended but also to illustrate the rationale behind the methods applied and direct observers to the origins thereof.

This project used the following resources for inspiration and instruction:

Tutorials

* [Getters and Setters in Python](https://www.geeksforgeeks.org/getter-and-setter-in-python/)
* [Nametuples in Python](https://www.freecodecamp.org/news/python-namedtuple-examples-how-to-create-and-work-with-namedtuples/)
* [Detect Key Press in Python](https://www.geeksforgeeks.org/how-to-detect-if-a-specific-key-pressed-using-python/)

Development Tools / Sources

_See technologies section for development environment and content generators / sources._

### Technologies

Development Environment
* [GitPod](https://www.gitpod.io/)
* [Drawio](https://www.diagrams.net/) + [Unofficial VSCode Plugin](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
* [Github](https://github.com/)
* [Heroku](https://heroku.com/)

Testing
* [PEP8 Checker](http://pep8online.com/)

Content Generators / Sources
* [Code Institute Python Environment Template](https://github.com/Code-Institute-Org/python-essentials-template)
* [Code Formatter](https://webformatter.com/)

Frameworks / Libraries
* [Gpsread for Python](https://gspread.org/)
* [Google Auth for Python](https://google-auth.readthedocs.io/en/master/)
* [Python-evdev for Python](https://python-evdev.readthedocs.io/en/latest/)

Languages
* [HTML5 - Included in Template](https://www.w3schools.com/html/)
* [CSS - Included in Template](https://www.w3schools.com/css/)
* [Javascript - Included in Template](https://www.w3schools.com/js/)
* [Python](https://www.w3schools.com/python/)

### Further Acknowledgements
The vibrant [Slack](https://slack.com/) community, cohort, tutors and my mentor Akshat Garg at [Code Institute](https://codeinstitute.net/).

[Code Institute](https://codeinstitute.net/), [FreeCodeCamp](https://www.freecodecamp.org/), [TheOdinProject](https://www.theodinproject.com/), and [W3Schools](https://www.w3schools.com/) for providing me with fundamental skills for software development.

[Prince2](https://www.axelos.com/certifications/propath/prince2-project-management) for the project management methodology.