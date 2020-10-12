<h3 style="text-align: center">
    <a href="https://github.com/sherylg343/thriller-books2">
        <img src="static/assets/images/navbar-logo.png">
    </a>
</h3>

<h1 style="text-align: center">
Find Thriller Book Community Website
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
a few well-thought out reviews rather than weeding through hundreds of them.  
As part of building the community, a forum will be one of the first features 
introduced in the next phase as it will offer a place for readers to share their
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
2. Functional: The users needs to easily find books by title or author, with
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
* email and passord inputs provide messages to affirm or correct inputs
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
* an erie full-cover background image was selected to create a first impression
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
* Book review forms are required to insure basic information is collected
so that the reviews provide value to readers. These required fields are
marked so user realizes they are required.
* A search criteria is required when searching for a book to provide
a more accurate book search for the user.

Local Storage:
* session storage is used to store user data for security reasons:
email, password and display name.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Future Goals <a name="future-goals"></a>
