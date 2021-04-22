# Spotify Song Getter and Texter

## Call Spotify API and send yourself a text message (SMS) containing the most recent song added to playlists by your friends. 

### Forthcoming frontend project(React.js) will allow you to add your phone number to receive weekly text of "top" songs from other users. This front-end will create new AWS Cloudwatch triggers with specific instructions and payloads to run app as serverless Lambda function. 

### Personal version hosted now on AWS. Beginning the process of scaling will be fun.

#### TO USE THIS AS OF NOW:

If you made it this far, thanks for taking an interest in this repository. In its current form, this app needs a little upfront work from the user:

1. First, you'll need to create developer's accounts and apps on both **Spotify** and **Twilio**. With your access credentials, load them as variables into your local environment in accordance with the outline found in the main.load_environment(); or into a .env file that you can create in the project's main directory(dotenv will do the work there if necessary).

2. Second, test.json needs to be filled out with some info. 

   * a. Add the usernames of your Spotify friends to be queried. To find your friends (or followers, or following), log into your personal account and copy and           paste their names into the file with double quotes around the name, and comma separate within the square brackets (the array) next to "dev_user_names"           (second line in file) like this: ["username1", "username2, "username3"]

   * b. Add the phone number you used to make your Twilio account in to the corresponding array for "dev_numbers". You can add more verified numbers manually. 
  
   * c. Add the app phone number that you selected when making a Twilio account and app.

3. Third, change the file name of *test.json* to *data.json*.

4. Fourth, make sure you've downloaded the package dependancies. Spotipy has been integrated for streamlining API calls, and the CacheHandler will store your API token in a hidden file, while the feature for client credentials handles the base64 encoding.

If the data is correctly insterted (look into more info on json if you must), and package dependancies are now available on you local environment, in your terminal, run python test.py

If it runs correctly, your console should print some songs, and your phone should receive them as well. If it doesn't, follow the yellow brick road.

