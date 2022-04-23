
# **WELCOME TO THE BIKESHARE README**

### **Table of contents**
   1. [Date of creation](#date)
   2. [Project Title](#project)
   3. [Description of the project](#description)
   4. [Presentation of the bikeshare](#presentation)
   5. [The Datasets used](#dataset)
   6. [How the program work ?](#work)
   7. [Software used](#soft)


## **1. Date of creation <a id="date"></a>**
   This project was created on 11th april 2022

## **2. Project Title <a id="project"></a>**
   Bikeshare big data analysis of three cities in American

## **3. Description of the project <a id="description"></a>**

   ![Divvy is a bicycle sharing system in the City of Chicago and two adjacent suburb](https://en.wikipedia.org/wiki/Divvy#/media/File:Bike_to_Work_Day_Rally.jpg)

   In this project, i have made use of **Python** to explore data related to bike share systems for three major cities in the **United States** : **Chicago**, **New York City**, and **Washington**. I have wrote code to import the data and answer interesting questions about it by computing **descriptive statistics.** I have also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

##  **4. Presentation of the bikeshare <a id="presentation"></a>**
### **4.1. Bikeshare Data**
   Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

   Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return  bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

   In this project, i have used data provided by [**Motivate**](https://www.motivateco.com/), a bike share system provider for many major cities in the **United States**, to uncover bike share usage patterns. You will compare the system usage between three large cities: **Chicago**, **New York City**, and **Washington, DC**.

## **5. The Datasets used <a id="dataset"></a>**
   Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
   * Start Time (e.g., 2017-01-01 00:07:57)
   * End Time (e.g., 2017-01-01 00:20:53)
   * Trip Duration (in seconds - e.g., 776)
   * Start Station (e.g., Broadway & Barry Ave)
   * End Station (e.g., Sedgwick St & North Ave)
   * User Type (Subscriber or Customer)

   The Chicago and New York City files also have the following two columns:

   * Gender
   * Birth Year

   You can download the file here : ([**Chicago**](https://www.citibikenyc.com/system-data) , [**New_York_City**](https://www.citibikenyc.com/system-data) , [**Washington**](https://www.citibikenyc.com/system-data) )

## **6. How the program work ? <a id="work"></a>**

   The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

   1. Would you like to see data for Chicago, New York, or Washington?
   2. Would you like to filter the data by month, day, or not at all?
   3. (If they chose month) Which month - January, February, March, April, May, or June?
   4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## **7. Software used <a id="soft"></a>**
I have used :
   * Python 3
   * NumPy, and pandas installed using Anaconda
   * A text editor Visual Studio code.
   * A terminal application


   
