# MILLION DOLLAR DIAGRAM

Below is a design diagram of the Application Programming Interface (API) that navigates through the ISS Sighting Data and returns relevant information based on the routes called by the user. This design diagram shows the different ways that a user can interact with the interface and reach the end of the program. There are three different avenues that a user can take when using this application.

![](https://raw.githubusercontent.com/Vjannu0711/COE332Jannu/main/homework07/MidtermCOE332.drawio.png)

**1) Reading the data from the file and also using the `help` function to understand the different API routes and what they output.**

In order to achieve this, simply run these three commands in the command line one-by-one:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5000
```
- Next, run `curl localhost:5000/read_data -X POST` which will display a message notifying the user that the data has been read.
- Next, run `curl localhost:5000/help` to take a look at what each of the routes do and output.

**2) Return the list of all of the EPOCHS as well as information for a specific epoch that is inputted by the user.**

In order to do this, run the first three commands as shown in the first avenue. 
- Run `curl localhost:5000/read_data -X POST` to read the data.
- Then run `curl localhost:5000/epochs` to return a list of all of the epochs.
- Then run `curl localhost:5000/epochs/<epoch>` with a specific epoch in the `<epoch>` section of the command.

**3) Return the list of all countries, regions, or cities, as well as all data for a specific country, region, or city.**

In order to do this, run the first three commands as shown in the first avenue.
- Run `curl localhost:5000/read_data -X POST` to read the data.
- Then `curl localhost:5000/countries` to return all of the countries.
- Then `curl localhost:5000/countries/<country>` with a specific country name in the `<country>` section of the command.

At this point, we can choose to end the program or we can run `curl localhost:5000/countries/<country>/regions` to display all of the regions in a specific country followed by `curl localhost:5000/countries/<country>/regions/<region>` that displays all of the sighting data for a specific region.

We can again choose to end the program here or go a step further by running `curl localhost:5000/countries/<country>/regions/<region>/cities` to display the list of all cities in a specific region followed by `curl localhost:5000/countries/<country>/regions/<region>/cities/<city>` to display all of the sighting data for a specific city.
