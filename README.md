# Breathe Easy

* [Project Page](https://2016.hackerspace.govhack.org/content/breathe-easy)
* [Submission Video](https://www.youtube.com/watch?v=oJ8S8FV0yag&feature=youtu.be)

REMARK

Each year, 1600 Australians die from exposure to air pollution. The life expectancy of Australians is diminished by an average 69 days on account of air pollution. Australia has the highest prevalence of Asthma in the world, with 1 in 10 people suffering from the chronic condition.

We all have the right to know about the quality of air we breathe and whether we are exposed to dangerous levels of pollution. The information empowers us to make decisions on whether to stay indoors or to relocate. Monitoring the quality of air can assist in determining the factors contributing to pollution. It is important to prevent air pollution from reaching toxic levels as seen in countries such as China and Mexico. Based on current emission trends, mortality due to outdoor air pollution is projected to double by 2050.
With the display of an interactive map that illustrates the levels of air pollution across Queensland, users are able to determine the levels of pollution in their current location. It clearly depicts the areas with poor to excellent air quality. The web application is responsive for easy use on both desktop and mobile.

The data sets integrated into the Breathe Easy App include a real-time feed of the air quality monitoring data, a list of all the monitoring sites with associated geographic information, and six NPI emission data sets containing industry emission data.
Within the Springboot application, the program is written in Groovy. Using the build tool Gradle, all the required data from the API servers were retrieved. The CSV files were converted into JSON documents to be loaded onto the MONGO no SQL database. The Springboot application was used as a framework to build the back-end API. Furthermore, the API for real-time data is called and reformatted into JSON documents to be passed to the front end. The Australian Government's Cloud service, NECTAR, hosts the APIs and front-end.
The front-end web interface is programmed in JavaScript, HTML and CSS, and served from Springboot. The open source libraries used were Bootstrap, J-Query, and the Google Map JavaScript API.
In the age of Internet Of Things, sensors have the potential to be implemented in a range of locations and monitor air quality. This crowdsourcing of data will be invaluable.


## Team Remark

* [Randall Fernando](https://github.com/rfern)
* [Richard Allwood](https://github.com/richard-allwood)
* [Michael Van Brummen](https://github.com/mvanbrummen)
* [Elizaveta Konovalova](https://github.com/ElizavetaKonovalova)
* [Rod Persky](https://github.com/Rod-Persky)
* [Kevin Ng](https://github.com/kevin-nkw)
* [Alexandra Tran](https://github.com/Alexandra1105)

## Requirements

Java and MongoDB

## Setup

Install MongoDB

To do.

## Explanation

To do.

## License

The MIT License (MIT)

Copyright (c) [2016] [Team Remark]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

