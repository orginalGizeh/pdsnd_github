import time
import datetime as dt
import pandas as pd
import numpy as np

choice_filter = ''

# var for storing the user's filter choice
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city,month,day = '','',''
    print('Hello! Let\'s explore some US bikeshare data!')
    print('*'*40)
    try:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        print("Would you like to see data for Chicago (ch), New York(ny), or Washington(wa) ? :  ")
        print()
        cities_dict = {'ch':'chicago', 'ny':'new york city', 'wa':'washington'}
        cities = pd.Series(cities_dict)
        while city not in cities:
            city = input("==> ").strip().lower()
            #get user input city even if he/she type for example ch or chicago
            if city in cities.index or city in cities.values:
                if city in cities.index:
                    city = cities_dict[city]
                print("City Accepted !")
                print()
                break
            else:
                print("The city inserted doesnt exist. Please enter one of the city stated above.\nChicago, New York, or Washington ")
                print()
                
        # get user input for filter's choice (month, day, both or none). HINT: Use a while loop to handle invalid inputs
        print("Would you like to filter the data by month, day, both, or not at all ? please type \"none\" for no time filter. :   ")
        print()
        list_choice_filter = ['month', 'day', 'both', 'none']
        choice_filter = ''
        while choice_filter not in list_choice_filter:
            choice_filter = input("==> ").strip().lower()
            
            if choice_filter in list_choice_filter:
                print("Filter\'s  choice Accepted !")
                print()
                break
            else:
                print("The filter\'s  choice inserted doesnt match. Please enter one of the choice stated above.\nMonth, Day, Both or None ")
                print()
    except:
        print("That's not a valid please ! Restart the program.")

    # get user input for month (all, january, february, ... , june)
    if choice_filter=='month':
        month = user_input_month()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif choice_filter=='day':
        day = user_input_day()
    elif choice_filter=='both':
        month = user_input_month()
        day = user_input_day()

    
    print('-'*40)
    return city, month, day, choice_filter

def user_input_day():
    """Manage the user input of day's value."""

    print("Enter the day you like to filter the data please. (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday) ")
    print()
    day=''
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while day not in days:
        day = input("==> ").strip().lower()
        print()
        if day in days or day=='all':
            print("Choice Accepted !")
            print()
            break
        else:
            print("The day inserted doesnt match. Please enter one of the choice stated above.\n(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday) ")
            print()
    return day

def user_input_month():
    """Manage the user input of month's value."""

    print("Would you like to filter the data by which month please ? ( January, February, March, April, May, June or All) ")
    print()
    month=''
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input("==> ").strip().lower()
        if month in months or month=='all':
            print("Choice Accepted !")
            print()
            break
        else:
            print("The month inserted doesnt match. Please enter one of the choice stated above.\n( January, February, March, April, May, or June) ")
            print()
    return month



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all' and month != '' and choice_filter!='none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all' and day !='' and choice_filter!='none':
        # use the index of the days list to get the corresponding int
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]


    """filter by month and day of week if applicable is directly exucetd when
        month and day contain value
    """

    return df


def time_stats(df, choice_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    input("Press Enter to print more stats")
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode().to_numpy()
    print("the most common month :" + str(common_month[0]))
    # display the most common day of week


    # display the most common start hour
    common_start_hour = df['hour'].mode().to_numpy()
    print("the most common start hour :" + str(common_start_hour[0]))
    print("Filter used : {}".format(choice_filter) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def station_stats(df, choice_filter):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    input("Press Enter to print")
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode().to_numpy()
    print("Most commonly used start station : " + start_station[0], "  Count : {}".format(df['Start Station'].value_counts()[0]))

    # display most commonly used end station
    end_station = df['End Station'].mode().to_numpy()
    print("Most commonly used end station : " + end_station[0])

    # display most frequent combination of start station and end station trip
    df['most_combination'] = df['Start Station'] + " => " + df['End Station']
    most_combination = df['most_combination'].mode().to_numpy()
    print("Most frequent combination of start station and end station trip : {}".format(most_combination[0]))
    print("Count : " + str(df['most_combination'].value_counts()[0]))

    print("Filter used : {}".format(choice_filter) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def trip_duration_stats(df, choice_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    input("Press Enter to print")
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time : {}".format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time : {}".format(mean_travel_time))

    print("Filter used : {}".format(choice_filter) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def user_stats(df, city, choice_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    input("Press Enter to print")
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print("Counts of user types \n{}".format(count_user))
    
    if city=='chicago' or city=='new york':
        # Display counts of gender
        count_gender = df['Gender'].value_counts()
        print("Counts of gender \n{}".format(count_gender))
        # Display earliest, most recent, and most common year of birth
        early_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode().to_list()[0]
        print("Earliest Year Birth : {}, Recent Year Birth : {}, Common Year Birth : {}".format(early_year,recent_year,common_year))

    print("Filter used : {}".format(choice_filter) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_trip_data(df):
    """Help for viewing the data loaded for analyzing. it only output 
    30 rows per request if the dataset has more than it"""

    print()
    #count number of rows
    count_rows = df.index.size

    input(".....Loading data........{} rows found......... (Press Enter to view)".format(count_rows))
    size = 30
    for i in list(range(0, df.index.size, size)):
        print(df[i:i + size])
        viewer = input("Would you like to view next thirty data ? Enter Yes or No : ")
        if viewer.lower() == 'no' or viewer == '':
            break

def main():
    while True:    
        city, month, day, choice_filter = get_filters()
        df = load_data(city, month, day)
        time_stats(df, choice_filter)
        station_stats(df, choice_filter)
        trip_duration_stats(df, choice_filter)
        user_stats(df,city, choice_filter)
        print_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    try:
	    main()
    except FileNotFoundError:
        print("The file that you are trying to use for analyzing doesn\'t exist.\nTry to check if the file exit in the directory, then restat the program. ")