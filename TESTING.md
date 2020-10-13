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
* The website has been tested on t browsers: Google Chrome, Safari and Firefox.
It was also tested on a variety of devices - iPhone 5, 8 and 10, 2014 and 2018 
iPads, and Mac laptop and desktop. The following issues were identified:
Safari: does not recognize reverse as an animation direction, so the fan icon 
will not rotate counterclockwise. Additionally, Safari is not recognizing changes 
in fan speed and Safari was showing Actual Temp. opaque on all devices, at all
times. The footer was not "sticky" in the desktop version of Safari as well.

* Firefox in a desktop browser performed without any problems as did Chrome.

* There were some issues with Apple devices as well. The 2014 iPad showed no 
functionality in the website. It did not respond to changes in inputs. The newer 
iPad did not have the same issues, it worked well except it was not filtering 
device selections in the Scheduler.

### Functionality Testing
Due to the nature of the website, the bulk of the testing was functional. The 
following describes the final round of functional tests conducted in Google 
Chrome using a MacBook Pro.
<br>