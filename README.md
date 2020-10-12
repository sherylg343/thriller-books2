<h3 style="text-align: center">
    <a href="https://github.com/sherylg343/thriller-books2">
        <img src="static/assets/images/navbar-logo.png">
    </a>
</h3>

<h1 style="text-align: center">
Find Thrillers Book Community Website
</h1>

<div style="text-align: center">

[View website deployed through Heroku](https://find-thrillers2.herokuapp.com/)
</div>

## Table of Contents <a name="table-of-contents"></a> 

1. [Project Purpose](#purpose)

2. [UX](#ux)

3. [Features](#features)

4. [Future_Goals](#future)

5. [Technology Used](#technology-used)

6. [Testing](#testing) - text in another document [TESTING](TESTING.md)

7. [Deployment](#deployment)

8. [Credits](#credits)

9. [Disclaimer](#disclaimer)

[Back to Top](#table-of-contents)


## Project Purpose <a name="purpose"></a> 
Find Thrillers is an organization founded by a group of friends who all enjoy
thriller and suspense novels. They wanted to develop an online community of readers who could share their love of books in the thriller/suspense genre.

### Project Goals
The long-term goal is to provide a number of alternative ways for readers to
find out more about the books they enjoy and engage with like-minded readers.
To facilitate the development of the community, the following features are 
planned: comprehensive book search, book reviews, forum for discussions about
books, authors and the thriller/suspense genre. Also, sharing of critic reviews
and a favorites section. Find Thrillers wants to be the place readers turn to, to 
find the next book to read or share about a book s/he just finished.

To continue to grow and develop, the site will require a revenue source. Two
options are being considered. One is a purchase button next to a book which is
similar to the ones on the NY Times Bestseller list - offering links to multiple
booksellers - from whom our website could collect a referral fee. Additionally,
advertising will be considered as our reader base grows.

### Target Audience
Readers who enjoy thriller and suspense novels, who speak/read English, are
targeted. Readers will vary in age but will have in common a love of reading
and books and a desire to share with others about the stories they have read.

<p>

[Back to Top](#Table-of-Contents)
</p>
---

## UX <a name="ux"></a>

### Targeted Visitors
Find Thrillers is targeting readers who are tired of scrolling through reviews on
sites such as Amazon and Barnes and Noble. They are looking for readers who 
enjoy this genre and want to read reviews by invested readers; preferring to read
a few well-thought-out reviews rather than weeding through hundreds of them.  
As part of building the community, a forum will be one of the first features 
introduced in the next phase, as it will offer a place for readers to share their
thoughts after reading a book - asking questions and sharing opinions. Find Thrillers
is looking to attract and draw in book lovers who want a place to share and
interact with others who share a similar interest.

### User Stories
1. As a reader of primarily thriller/suspense novels, I'm looking for a website to find
the best stories in the genre, so I don't waste my time on poorly written books.
2. As a reader of primarily thriller/suspense novels, I want to share my opinions 
about the books I've read, to help others select the best books to read.
3. As a reader of primarily thriller/suspense novels, I want to easily find new 
books to read by my favorite authors, as well as new ones, so that I don't waste
my time looking for or reading books I don't enjoy.
4. As an occasional reader of thriller/suspense novels, I want to find the best
in the genre books to read in my limited spare time, accessing thoughtful reviews
and book suggestions, so that I thoroughly enjoy the books I read.
5. As a participant in the Find Thrillers community, I want to be able to View
the reviews I've written and change or delete them if I change my mind about a 
book I've read.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Features <a name="features"></a>

### Use of Five Planes of UX in Project Design
#### Strategy Plane
An evaluation was conducted to determine which customer needs the website should
address first. These customer needs are listed and reviewed in the 
[Strategy Trade-Off Analysis](Readme-assets/strategy-trade-off.pdf). Prior to 
developing this analysis, the following competitor websites were viewed and
evaluated: Amazon, Goodreads and BarnesandNoble.

#### Scope Plane
Below is a summary of the analysis done for this website during the Scope Plane.
1. Objective: The user wants a resource to help him/her select a book to read
that will be very enjoyable and ensures that the selection be done quickly and
efficiently. The user also wants to assist others in doing the same, by providing
helpful reviews of books previously read.
2. Functional: The users need to easily find books by title or author, with
accompanying reviews, as well as find a list of recommended books that will 
rotate and change.
3. Non-functional: the number of reviews will be limited until the quantity
of users grows - so the developers of Find Thrillers will need to provide
many of the initial reviews in order to provide value that will prompt the 
users to return.
4. Business Rules: resources, both human and financial, are limited at this
time so important features that are not easily implemented will need to
wait until phase 3, including: community forum, a contact form to 
correspond with site administrator, access to critic reviews, and link to
purchase a book.

#### Structure Plane
Below are the key considerations relative to the Structure Plane.
1. Consistency: 
* the search bar is at the top of each page on website - always accessible
and identical in layout.
* the fonts and styling for text and headlines is consistent from page to
page.
* the navigation bar is sticky so appears at the top of each page in an
identical fashion.
* all pages are designed with white cards or forms on a gray background
that blends with the cover image on index page.
2. Predictable:
* helper text is provided under the password and display name input
fields to assist user in creating account with ease
* the edit book review form is laid out the same as the original book
review form, for ease of use.
* buttons are clearly labelled, e.g. "submit review, delete, edit"
3. Learnable:
* flash message capability is enabled for every page to assist user,
providing feedback for actions such as, creation of account, logging in,
logging out, submission of a review, as well as error messages when
an action does not go as planned.
* email and password inputs provide messages to affirm or correct inputs
* if a user tries to review a book for a second time, a message flashes
across the top of the page informing user that s/he has already reviewed
that specific book and redirects user to their book reviews page.
4. Visible:
* navigation menu changes once a user logs in - so options not available
to a user not logged in are not visible or actionable.
* inputs and action buttons are large and well-labelled
5. User Feedback: 
* log in fields change color during input
* flash messages occur at top of page to inform user of successful or
unsuccessful completion of actions

#### Skeleton Plane
Usability: the card layout was selected to depict a book and is used
consistently throughout the site to display the same information: 
* book search results
* book profile
* book review form
It was deemed important for the books to look the same, so the 
horizontal design and consistency of the book cards appearing one per row,
even in large screens, was decided to assist the user. Multiple book
cards could have been placed in a row on a large screen, but con-
sistency would have been sacrificed, and it was decided this was
not have been in the user's best interest.

#### Wireframe Mock-Ups:
After reviewing the User Stories and evaluating the Features, the following
mockups were designed for the 3 primary screen sizes using 
[Balsamiq software](https://balsamiq.com/). 
The website was created using a mobile-first design philosophy.

<div style="text-align:center;">

[Mobile](README-assets/mobile-books-final.pdf)
</div>

<div style="text-align:center;">

[Tablet](README-assets/ipad-books-final.pdf)
</div>

<div style="text-align:center;">

[Desktop](README-assets/desktop-books-final.pdf)
</div>

##### Wireframe Mock-Up Revisions
1. After designing the wireframe mock-ups and experimenting with
both Start Bootstrap and Materialize, I determined a Materialize card
layout to use throughout the website to depict a book's information.
To maintain consistency in the card, it was decided to maintain one
card per row at all screen sizes.
2. To minimize user confusion, a separate page was created to
create an account, instead of combining it with a login page.

#### Surface Plane
1. Background: 
* an eerie full-cover background image was selected to create a first impression
for a site visitor, as well as a welcome message explaining the purpose of 
the site.
* a color palette to coordinate with the image as well as a theme of "mystery"
was selected: black, shades of gray, yellow, dark teal and white.
* all input fields are white, so a background of gray was selected so they
are easily identified and provide a soothing color-coordinated background.
2. Fonts:
* selected by Materialize, but chose not to over-ride them as they were
easy to read and eye-catching.
* when gray background was applied, readability did suffer, so font-weight
for the site was increased to 700 universally.
3. Images/Icons:
* Jumbotron image selected to attract attention and correspond with theme
of thriller/suspense novels
* book images featured in book cards - image was important to include
whenever a book is featured to improve look of web pages and give reader
an image to tie to a book
4. Controls:
* all controls are brightly colored and carefully-worded links and buttons
to facilitate easy use and avoid confusion

### More on Features
Navigation: A sticky navigation bar with a dropdown menu for account links
provides easy access to all sections of the website wherever the user is.
A mobile version has a menu icon and side navbar for ease of use.

Defensive Design: as mentioned previously, this was a key concept considered
in designing the website and to facilitate ease and pleasure of use.
Testing by users unfamiliar with the site, provided additional ideas for
defensive design enhancements that were added later in design phase.
* Access to book review form and accompanying review pages are accessible
only if a user is logged in. These pages are not even visible on the
navigation bar unless the user is logged in.
* Field requirements are listed below input field for password and 
display name fields and html validation prevents acceptance of input
data that does not conform to requirements.
* Before a user can complete a book review, it is checked to insure the
user is logged in and has not already completed a review for the book.
* Error message are built in if the website is not able to connect with
the Google Book API so the error code with print to the terminal and
a flash message will display to the user.
* Werkzeug security was employed to protect user passwords when storing
them in a user database.
* Book review forms are required to ensure basic information is collected
so that the reviews provide value to readers. These required fields are
marked so user realizes they are required.
* A search criterion is required when searching for a book to provide
a more accurate book search for the user.

Local Storage:
* session storage is used to store user data for security reasons:
email, password and display name.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Future Goals <a name="future-goals"></a>

### Display review count and average rating
As reviews become more numerous, it would be helpful to count and average
the ratings in the reviews for each book and display prior to the
individual reviews. This is one of the first additions recommended
for the website.

### Provide a contact form for users
Establish a "Contact Us" section so users have a form they
can access to contact the site administrator with any questions or
concerns.

### Initiate a Community forum
Providing a community forum to discuss books, authors, plots, etc.
will help build a sense of community among the users. This is an
important feature to add for the mission of the website.

### Truncate book descriptions and long reviews and include a "Read More" link or button
This would provide a cleaner website and the user would see more information
without having to scroll down. This feature would improve usability.

### Include a Password Reset on User Profile page
This is a basic feature necessary for users to reset password if they
lose it.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Technology Used <a name="technology-used"></a>

## Languages, Frameworks, Editors & Version Control:
* HTML & CSS programming languages
* [Materialize](https://materializecss.com/) - used to help make the website 
designed for mobile-first, responsive to all screen sizes and visually appealing
* [Python](https://www.python.org/) - used with Flask to operate website
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - framework used in 
conjunction with Python to operate website
* [jQuery](https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js) 
* JavaScript - used with jQuery for functionality of website
* [GIT](https://git-scm.com/) - Version Control
* [GITHUB](https://github.com) - to host the repositories for this project and 
the live website preview


## Tools Used:
* [MongoDBAtlas](https://www.mongodb.com) - document database hosting service used
* [GoogleBooks](https://developers.google.com/books) - API used to enable book
searching on site
*[Heroku](https://www.heroku.com/home) - used to deploy nonproduction version of
website
*[GoogleChromeDevTools](https://developers.google.com/web/tools/chrome-devtools) -
used to test and troubleshoot the functionality of the website and assist in
visual styling decisions, especially relative to screen sizes
* [GoogleFonts](https://fonts.google.com/) - Noto Sans JP and Hind Siliguri 
Font Styles
* [tinyjpg](https://tinyjpg.com/) - used to reduce image file sizes
* [FontAwesome](https://fontawesome.com/) - Design icons for Services 1 page and 
social media icons
* [BeautifyTools](http://beautifytools.com/javascript-validator.php) - used to 
validate JavaScript code and format/beautify all code
* [Nu_html_checker] (https://validator.w3.org/) - html validator
* [JSHint](https://jshint.com/) - JavaScript validator that recognizes jQuery
* [JSDoc](https://jsdoc.app/) - for comments in JavaScript file
* [stackOverflow][https://materializecss.com/] - questions forum helped with
troubleshooting code

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Testing <a name="testing"></a>
Testing can be found in a separate file - [TESTING.md](TESTING.md)

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Deployment <a name="deployment"></a>
The following steps were taken to deploy my GitHub repository using Heroku.

### In GitHub Repository do the following:
1. Install all required modules using "pip3"
2. Create an env.py file and make sure it is listed in your .gitignore file.
Format of entries should follow this example:
after listing "import os" at the top of the file:
os.environ.setdefault("MONGO_DBNAME", "thriller_books")
3. Add all important project variables, such as PORT, IP, API Key, Secret Key, 
database name, and database url
4. Type the following at the top of the app.py file:
if os.path.exists("env.py"):
    import env
5. For each environmental variable, define the variable (such as API_KEY) 
as follows in the app.py file:
API_KEY = os.environ.get('API_KEY')
6. Once all necessary modules are installed in repository and env.py file is
complete, create a Requirements.txt file listing all installed modules by 
typing the following into the terminal after the $ prompt: 
pip3 freeze --local > requirements.txt
7. Create a Procfile that will tell Heroku how to run the project.
Type the following into the terminal after the $ prompt: 
echo web: python app.py > Procfile
8. Confirm both files have been added to the directory of the repository.
9. Add, commit and push changes in repository to GitHub

### On Heroku website do the following:
1. Create an account or sign into an existing account
2. Click on "New" button and create a new app with a unique name
3. Once created, click on app name and then click on Settings in menu bar at top
of page
4. In middle of page, in "Config Vars" section, click on box that reads, 
"Reveal Config Vars"
5. In that section with be "key" and "value" input boxes. For all
applicable variables, such as PORT, IP, API Key, Secret Key, database name,
and database url, input key and value and click "add".
6. Once all variables have been input, click on "Deploy" in menu bar.
7. In "Deployment Method" section, click on "GitHub"
8. Under section heading "Search for a repository to connect to,"
type in repository name following GitHub display name and hit return
or the "Search" button.
9. The name of the repo found in GitHub will be printed below,
click on the "Connect" button across from it, if it is correct.
10. The app is now connected to the specified GitHub repository.
11. To enable automatic deployment, scroll down to "Automatic Deploys"
section and click on button "Enable Automatic Deploys."
12. In menu button, click on "Settings" and scroll down to section
titled "Domains" and you will find your domain address:
Your app can be found at https://find-thrillers2.herokuapp.com/
13. After instigating automatic deployment, all changes committed
to the GitHub repository will be reflected in the deployed site on
Heroku.

### How to Run this Project Locally
To run the project locally, make a clone of it from GitHub:

1. Working from the GitHub repository page, find the green button on right 
labeled **Clone or download** and click it to open a dropdown menu.
2. Below the headline **Clone with HTTPS** is a web address, click on the 
button to the right of it to copy the link.
3. In your local IDE open Git Bash.
4. Change the current working directory to the location where you want to 
place the cloned directory.
5. Type ```git clone```, then paste the clone URL address copied in step 2 
as follows:
```console git clone https://sherylg343.github.io/smarthome/```
6. Press enter to finish creating the local clone.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Credits <a name="credits"></a>

### Images
Image and Icons (not from Google books) were free and found on the 
following websites:
* [FontAwesome](https://fontawesome.com/) 
*[shutterstock](https://www.shutterstock.com/)

### Contents
All copy was written by developer.

### Code
* The star rating was taken from [jsfiddle]( https://jsfiddle.net/8cn2mekf/8/)
* Additional resources used for snippets of code are marked above the corresponding 
code in the CSS and JavaScript files.


### Acknowledgements
Many thanks to Code Institute tutors and alumni who provided assistance
throughout the development phase, with special appreciation extended towards:

* Brian Mancharia - mentor; Brian provided extraordinary guidance and 
insight that enabled me to tackle this project.
* Code Institute Tutors: Michael, Samantha, Scott, Anna, Roman, Michael and Igor
with special thanks to Tim for not only his assistance but also sharing the 
new task manager videos with me.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Disclaimer <a name="disclaimer"></a>
Please note the content and images on this website are for educational purposes only.

<p>

[Back to Top](#Table-of-Contents)
</p>