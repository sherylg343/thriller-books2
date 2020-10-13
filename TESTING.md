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

## Testing

### Ongoing Testing
* Throughout development of the website, Google Chrome Developer Tools were used
to track changes and troubleshoot problems. The terminal proved invaluable in
troubleshoot Python code.
* The Materialize footer has been troublesome from the beginning. I commented
it out, deciding to deal with it later. A container class caused it to 
scroll horizontally and once that was removed it started floating up when
content wasn't available to push it to the bottom. Affter duplicating all
suggested code in Materialize's documentation, the footer would not move
to the bottom of the page and it was creating significant left and right
margin issues for the search bar and flash message sections of the base.html
code. After online research, also tried positioning footer absolutely, which
did not work either. So given that only social media links, a copyright and
terms and conditions link were in footer - it was left out at this time.
* At the end of the development process, 
[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
and [Nu Html Checker](https://validator.w3.org/) were used. 
 - CSS: The validation did not recognize the CSS variables being used so there 
 were numerous errors listed. As the variables are integral to the website 
 design and operation, and were found documented by [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), 
 they were not changed. Another error message addressed fonts unknown -
 an unknown vendor extension. Given these fonts were established by
 Materialize, and all appropriate CDN links were pasted into the document,
 the errors were also ignored.
 - HTML: This validator identified a couple of errors that were corrected:
 1. Both the search bar and flash messages below the navigation were wrapped
 in section tags which did not include header tags(as were recommended in
 documentation). The section tags were removed for both of these to comply
 with the documentation. 
 2. Image tags for the book covers did not have alternative text so that 
 was added.
 3. A table that was being iterated over for reviews had an id that was
 being duplicated so it was changed to a class.

 ### Browser and Device Evaluations
* The website has been tested on three browsers: Google Chrome, Safari and Firefox.
It was also tested on a variety of devices - iPhone 5, 8 and 10, iPads, and 
Mac laptop and desktop. No major issues were identified.

### Functionality Testing
Due to the nature of the website, the bulk of the testing was functional. The 
following describes the final round of functional tests conducted in Google 
Chrome using a MacBook Pro - so nav bar was not collapsed.
<br>

#### Part One: Initial Navigation 

**Test #: 1**
<p>
Action Taken: Click on "Featured Books" in Nav bar
<br>
"Before" State: "Featured Books" in yellow text
<br>
"After" State: Screen jumps down to "Featured Books" section on the home page
<br>
Test Result: Successful
</p>

**Test #: 2a**
<p>
Action Taken: Click on "Create Account" in Nav bar
<br>
"Before" State: Missing
<br>
"After" State: No change
<br>
Test Result: Unsuccessful, changed text back to yellow and repeated tested
</p>

**Test #: 2b**
<p>
Action Taken: Click on "Create Account" in Nav bar
<br>
"Before" State: "Create Account" in yellow text
<br>
"After" State: Jumped to "Create Account" web page
    <br>
Test Result: Successful
</p>

**Test #: 3**
<p>
Action Taken: Click on "My Account" in Nav bar
<br>
"Before" State: "Log In" appears in teal text, clicked on "Log In"
<br>
"After" State: "Log In" page appears
<br>
Test Result: Successful
</p>


#### Part Two: Create Account
**Test #: 4**
<p>
Action Taken: Click on Email field
<br>
"Before" State: Icon, label and bottom border of input are gray
<br>
"After" State: State: Email label jumps up to allow for data entry and
label and line at bottom of input turn green
<br>
Action Taken: Click somewhere else before finishing
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Bottom border line turns red and message
appears below input "please input a valid email address"
<br>
Action Taken: Input a valid email address and hit enter
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Message appears below input "Email is formatted correctly"
<br>
Test Result: Successful
</p>

**Test #: 5**
<p>
Action Taken: Click on Password field
<br>
"Before" State: Icon, label and bottom border of input are gray,
Message below input field states "Password must consist of 6 to 15
numbers or upper/lower case letters - no spaces or special characters"
<br>
"After" State: State: Password label jumps up to allow for data entry and
label and line at bottom of input turn green
<br>
Action Taken: Click somewhere else before finishing
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Bottom border line turns red and message
appears below input "password is not formatted correctly"
<br>
Action Taken: Input a valid password and hit enter
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Message appears below input "Password is formatted correctly"
<br>
Test Result: Successful
</p>

**Test #: 6**
<p>
Action Taken: Click on Display Name field
<br>
"Before" State: Icon, label and bottom border of input are gray,
Message below input field states "Display Name must consist of 6 to 15
numbers or upper/lower case letters - no spaces or special characters"
<br>
"After" State: State: Label and line at bottom of input turn green
<br>
Action Taken: Click somewhere else before finishing
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Bottom border line and label turns gray
<br>
Action Taken: Input a valid display name and hit enter
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Enter triggers submission of account and redirected
back to home page and a message across the top states "Account
Creation Successful - You are Logged In"
<br>
Test Result: Successful
</p>

#### Part Three: Log In

**Test #: 7**
<p>
Action Taken: Click on Email field
<br>
"Before" State: Icon, label and bottom border of input are gray
<br>
"After" State: State: Email label jumps up to allow for data entry and
label and line at bottom of input turn green
<br>
Action Taken: Click somewhere else before finishing
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Label and bottom border turn back to gray
<br>
Action Taken: Input a valid email address and hit tab
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Email label turns gray and input bottom border
remains green
<br>
Test Result: Successful
</p>

**Test #: 5**
<p>
Action Taken: Click on Password field
<br>
"Before" State: Icon, label and bottom border of input are gray
<br>
"After" State: State: Password label jumps up to allow for data entry and
label and line at bottom of input turn green
<br>
Action Taken: Click somewhere else before finishing
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Bottom border line and label turn back to gray
<br>
Action Taken: Input a valid password 
<br>
"Before" State: Email label and bottom border are green
<br>
"After" State: Email label and bottom border are green
<br>
Test Result: Successful
</p>

**Test #: 6**
<p>
Action Taken: Click on Log In button
<br>
"Before" State: Input field labels and bottom borders are green and
input fields are filled with inputted email and password
<br>
"After" State: Redirected to "gorgesnlakes's Profile Page", message
across the top states, "Welcome, gorgesnlakes"
<br>
Test Result: Successful
</p>

#### Part Four: Other My Account Pages

**Test #: 7**
<p>
Action Taken: Click on "My Book Reviews" in "My Account" Dropdowm Nav menu
<br>
"Before" State: "My Book Reviews" in teal text on black background
<br>
"After" State: Redirected to "gorgesnlakes's Book Reviews" page
<br>
Test Result: Successful
</p>

**Test #: 8**
<p>
Action Taken: Click on "My Profile" in "My Account" Dropdowm Nav menu
<br>
"Before" State: "My Profile" in teal text on black background
<br>
"After" State: Redirected to "gorgesnlakes's Profile Page"
<br>
Test Result: Successful
</p>

**Test #: 9**
<p>
Action Taken: Click on "Log Out" in "My Account" Dropdowm Nav menu
<br>
"Before" State: "Log Out" in teal text on black background
<br>
"After" State: Redirected to "Log In" page with message at top reading,
"You have been logged out"
<br>
Test Result: Successful
</p>

#### Part Five: Book Search

**Test #: 10**
<p>
Action Taken: Click on "Choose search type first" dropdowm menu in 
search bar section at top of page, choose "Title"
<br>
"Before" State: "Title" in teal text on white background in dropdown
menu
<br>
"After" State: Title in black in dropdowm menu field
<br>
Action Taken: Click in search bar and type "Gone Girl"
<br>
"Before" State: white input field with "search" label at top left
of search field
<br>
"After" State: "Gone Girl" in black type in search field
<br>
Option 1: Action Taken: Click on search icon button
<br>
"Before" State: white button with search icon on it
<br>
"After" State: Redirected to "Search Results" page
<br>
Option 2: Action Taken: Hit enter button
<br>
"Before" State: all fields filled as stated above
<br>
"After" State: Redirected to "Search Results" page
<br>
Test Result: Successful
</p>

**Test #: 11**
<p>
Action Taken: Scroll down and click on "Write A Review" link in the
"Pretty Girl Gone" book by David Housewright card on "Search Results" page
<br>
"Before" State: "Write A Review" in gold text on white 
background in card
<br>
"After" State: Redirected to "Book Review Form" page for "Pretty Girl Gone" by
David Housewright
<br>
Test Result: Successful
</p>

#### Part Six: Book Profile

**Test #: 12**
<p>
Action Taken: Click on "Book Profile & Reviews" link in the
"Gone Girl by Gillian Flynn" book card on "Search Results" page
<br>
"Before" State: "Book Profile & Reviews" in teal text on white 
background in card
<br>
"After" State: Redirected to "Book Profile" page for "Gone Girl" by
Gillian Flynn
<br>
Test Result: Successful
</p>

**Test #: 13**
<p>
Action Taken: Click on "Write A Review" link in the
"Gone Girl by Gillian Flynn" book card on "Book Profile" page
<br>
"Before" State: "Write A Reviews" in gold text on white 
background in card
<br>
"After" State: Redirected to "ssg88's Book Reviews" page with
message across the top of page stating "You have already submitted
a review for this book. You may edit or delete it below."
<br>
Test Result: Successful
</p>


#### Part Seven: Book Review Form

**Test #: 14**
<p>
Action Taken: Click on "Choose search type first" dropdowm menu in 
search bar section at top of page, choose "Author"
<br>
"Before" State: "Author" in teal text on white background in dropdown
menu
<br>
"After" State: Author in black in dropdowm menu field
<br>
Action Taken: Click in search bar and type "Daniel Silva"
<br>
"Before" State: white input field with "search" label at top left
of search field
<br>
"After" State: "Daniel Silva" in black type in search field
<br>
Action Taken: Hit enter button
<br>
"Before" State: all fields filled as stated above
<br>
"After" State: Redirected to "Search Results" page
<br>
Test Result: Successful
</p>

**Test #: 15**
<p>
Action Taken: Scroll down and click on "Write A Review" link in the
"The Heist" book card 
<br>
"Before" State: "Write A Reviews" in gold text on white 
background in card
<br>
"After" State: Redirected to "Book Review Form" for "The Heist" by
Daniel Silva
<br>
Test Result: Successful
</p>

**Test #: 16**
<p>
Action Taken: Scroll down and clicked on the far right star for a 
5-star rating
<br>
"Before" State: 5 gray stars
<br>
"After" State: 5 gold stars
<br>
Test Result: Successful
</p>

**Test #: 17**
<p>
Action Taken: Entered "A Good One!" as review title
<br>
"Before" State: white input field with light gray placeholder text
of "Review Title"
<br>
"After" State: "A Good One!" typed in field and border below input 
is green
<br>
Test Result: Successful
</p>

**Test #: 18**
<p>
Action Taken: Entered "Enjoyed the story, another suspenseful Gabriel
Allon plot!" as review
<br>
"Before" State: white input field with light gray placeholder text
of "Enter your review here"
<br>
"After" State: "Enjoyed the story, another suspenseful Gabriel
Allon plot!" typed in field and border below input is green
<br>
Test Result: Successful
</p>

**Test #: 19**
<p>
Action Taken: Clicked on dropdown menu next to "Does your review
contain spoilers?" and selected "No"
<br>
"Before" State: white dropdown menu with type of "Choose..."
<br>
"After" State: "No" is value in dropdown menu field
<br>
Test Result: Successful
</p>

**Test #: 20**
<p>
Action Taken: Click on "Submit Review" button
<br>
"Before" State: yellow "Submit Review" button and all form fields
filled in
<br>
"After" State: Redirected to "ssg888's Profile Page" with message
at top stating, "Thank you for submitting your review. You may View
it by scrolling down this page."
<br>
Test Result: Successful
</p>

#### Part Eight: Edit Book Review
**Test #: 21**
<p>
Action Taken: On Profile Page, scroll down to view book review
just entered for "The Heist" and click on teal "Edit" button
<br>
"Before" State: teal "Edit" button next to red "Delete" button
<br>
"After" State: Redirected to "Edit Book Review" page, with fields
filled in with current "The Heist" review
<br>
Test Result: Successful
</p>

**Test #: 22**
<p>
Action Taken: On edit form, scroll down to change rating from
5 to a 4
<br>
"Before" State: input field below "*My Rating(click to rate):"
was "5"
<br>
"After" State: rating value changed to "4"
<br>
Action Taken: click on yellow button "Submit Edit"
<br>
"Before" State: yellow button says "Submit Edit"
was "5"
<br>
"After" State: redirect to "ssg888's Book Reviews" page
<br>
Test Result: Successful
</p>