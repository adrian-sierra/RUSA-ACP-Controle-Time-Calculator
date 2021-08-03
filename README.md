This application is a variation of the RUSA ACP controle time calculator.

The difference between this implementation and that one is that we will be using AJAX to automatically populate the appropriate open and close times of a control on a given brevet, and also provided a starting date and time by the user.

The options for brevet distances are 200km, 300km, 400km, 600km, and 1000km.

Uses arrow library to alter and display the date and time string format back and forth between frontend and backend implementations.

Times are altered according to the rules already put in place by the organization and made available to the rest of the public.

The added functionality put in place was storing the calculated closed and open times for each control in a database, using MongoDB, and having two buttons; a "Submit" and a "Display" button.

The "Submit" button, when clicked, would send the open and close times to the database, and reload the html page with empty entries. Another thing to note, is that this implementation chose to reset the database entries after every submit, this was done to simulate the a single brevet race, as opposed to many entries for all sorts of brevet distances.

The "Display" button, when clicked, would display the data in the database in the same html page that the user entered the control distances for the brevet distanced race. Again, paired with the implementation of the "Submit" button, this implementation takes in a sole entry of controls for a single brevet distanced race, as mentioned for the "Submit" button functionality.

TEST CASES: Two such error cases are dealt with in this implementation. Errors were handled through flask flash messages and displayed to the user on the same html page that the control entries are entered.

One of the possible handled errors, is when a user attempts to submit to the database an empty data table which has no calculated open and close times, and an error message "ERROR: Trying to add empty data" will be displayed to the user to notify them of their erroneous actions. Again, upon clicking the "Submit" button, the data in the database is cleared, so clicking "Submit" with empty data, won't impact the database entries, it just empties the database every time the button is clicked, but this causes no issues with displaying data as the functionality of this particular implementation has mentioned above.

The other handled error is very much similar to the above error case, but only now with the "Display" button, and displays the message "ERROR: Trying to display empty data" to the user in the same fashion through flask flash messahes onto the same html page.

This particular implementation mitigates many possible errors because of the fact of clearing the database upon clicking "Submit", and the reason behind this particular implementation has been explain above, and is seen as better by the developer because it imitates real life use of this variation of the RUSA ACP controle time calculator.

Simple listing from mongodb database, and specifically the open and close times that are calculated in specified formats based on the corresponding URLs.

Implemented service to expose times in database of all the times, open only, and close only.

For all, open only, and close only times, we returned, expose, and added API for them in JSON format.

For URLs specifying csv format, the corresponding times were returned in csv format by knowing which times are being returned and appropriately formatting the times in return statement.

For top "k" implementation, we request the added top=num from the URL in the get method for corresponding open, close times and indexing that specific input number when returning the appropriate time in the specified data format, be it either JSON or csv format.

Last functionality implemented was the consumer program which uses the service exposed in each API. This was implemented through php file and getting the contents of appropriate container URLs and echoing the corresponding contents onto an html page. This functionality was applied for exposing all, open only, and close only times using different formatting and scripts for each exposure.

Functionality was also added to Dockerfile and docker compose yml file that bridged together the containers of the brevet functionality, database functionality, and website that uses the times that were exposed.

In order to build the containers and run this application on your own, first, create a directory named "templates" and place the "404.html" and the "todo.html" file in that directory. Create another directory named "website" and place the "index.php" file in that directory. Create another directory named "static" and create a subdirectory named "js" and place the "moment.min.js" file that "js" subdirectory. Once you are in the main directory, you can use "docker-compose -f docker-compose.yml up" to build the appropriate containers. After everything has been built, simply go to localhost:5000 to input controls and get times out, submit to database using the submit button, then enter whichever service you want expose (e.g. localhost:5000/listAll). If you want the see the consumer program, go to localhost:5001.

Docker download: https://www.docker.com/products/docker-desktop
