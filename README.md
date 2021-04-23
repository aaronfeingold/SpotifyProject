# Spotify Song Getter and Texter

## Call Spotify API and send yourself a text message (SMS) containing the most recent song added to playlists by your friends. 

### Forthcoming frontend project(React.js) will allow you to add your phone number to receive weekly text of "top" songs from other users. It will create new AWS Cloudwatch triggers with specific instructions and payloads to run app as Lambda function. 

### Personal version hosted now on AWS.

#### TO USE:

If you made it this far, thanks for taking an interest in this repository. In its current form, this app needs a little upfront work from the user:

1. First, you'll need to create developer's accounts and apps on both **Spotify** and **Twilio**. With your access credentials, load them as variables into your local environment; or into a .env file that you can create in the project's main directory(dotenv will do the work there if necessary).

2. Second, test.json needs to be filled out with some info. 

   * a. Add the usernames of your Spotify friends to be queried. To find your friends (or followers, or following), log into your personal account and copy and           paste their names into the file with double quotes around the name, and comma separate within the square brackets (the array) next to "dev_user_names"           (second line in file) like this: ["username1", "username2, "username3"]

   * b. Add the phone number you used to make your Twilio account in to the corresponding array for "dev_numbers". You can add more verified numbers manually. 
  
   * c. Add the app phone number that you selected when making a Twilio account and app.

3. Third, change the file name of *test.json* to *data.json*.

4. Fourth, in your terminal, run: 
    > $ pipenv install

5. If the data is correctly inserted, and package dependencies are now available on you local environment, in your terminal, run the test:
    > $ python main.py
    > 

6. Last, your console should print either done or errors; your phone should receive a text message with links to--potentially--good music.
