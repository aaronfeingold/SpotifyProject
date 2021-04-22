# Spotify Song Getter and Texter

## Call Spotify API and send yourself a weekly text containing the most recent song added to playlists by your friends. 

### Forthcoming frontend project(React.js) will allow you to add your phone number to receive weekly text of "top" songs from other users. 

### Hosted on AWS Lambda with Cloudwatch triggers for personal usage now. Beginning to process of scaling.

#### TO USE AS OF NOW:

If you made it this far, thanks for taking an interest in this repository. In its current form, this app needs a little upfront work from the user.

First, you'll need to create developer's accounts and apps on both Spotify and Twilio. With your access credentials, load them as variables into your local environment in accordance with the outline found in the main.load_environment(); or into a .env file that you can create in the project's main directory(dotenv will do the work there if necessary).

Second, test.json needs to be filled out with some info. 

  a. Add the usernames of your Spotify friends to be queried. To find your friends (or followers, or following), log into your personal account and copy and paste their names into the file with double quotes around the name, and comma separate within the square brackets (the array) next to "dev_user_names" (second line in file) like this:

  ["username1", "username2, "username3"]

  b. Add the phone number you used to make your Twilio account in to the corresponding array for "dev_numbers". You can add more verified numbers manually. 
  
  c. Add the app phone number that you selected when making a Twilio account and app.

Third, change the file name of test.json to data.json.

Fourth, make sure you've downloaded the package dependancies. Spotipy has been integrated for streamlining API calls.

If the data is corrected insterted (look into more info on json if you must), and package dependancies are now available on you local environment, in your terminal, run python test.py

If it runs correctly, your console should print some songs, and your phone should receive them as well. 

