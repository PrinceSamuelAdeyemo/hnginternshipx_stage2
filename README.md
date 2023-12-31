HOW TO SET UP THE API
You can set up by visiting the address https://honeywell.pythonanywhere.com/api/ and then you are quick to get started.
NOTE: user_id == name
so when you using the api, the user_id will be replaced with the name to be used.

RUNNING THE CODE
Since this API provides that functionality for the CRUD request.

+ CREATE PERSON (post request)
We will start with the post request (CREATE 'PERSON/USER')
*if you are using a browser or anything
- Connect to this api with https://honeywell.pythonanywhere.com/api/
- You will be directed to the input box to input the name
- Add the user's name
- Click on the POST

*If you are using the testing script, you can automatically add the 'name' attribute in your data key.

- If the name contains only strings, then the next step will occur, else, you will receive a response for invalid input parameter and no name will be created.
- The name will be created with the post request you made.


+ READ PERSON (get request)
- Connect to this api with you query parameter which will be added by default with https://honeywell.pythonanywhere.com/api/<user_id>
- If the user is saved in the database, then there will be a response that will be in the output, the response should be the name of the user_id which you passed, but if the user is not saved in the database, then 'Invalid Input Parameter' will be the output.

+ UPDATE PERSON (put request)
- Connect to this api with you query parameter which will be added by default with https://honeywell.pythonanywhere.com/api/<user_id>
*if you are using a browser or anything.
- Connect to this api with https://honeywell.pythonanywhere.com/api/<user_id>
- You will be directed to the input box to input the name
- Add the user's name
- Click on the PUT
- If the user is saved in the database, then there will be a response that will be in the output, the response should be the name of the user_id which you passed to replace an existing data, but if the user is not saved in the database, then 'Invalid Input Parameter' will be the output.


+ DELETE PERSON (delete request)
- Connect to this api with you query parameter which will be added by default with https://honeywell.pythonanywhere.com/api/<user_id>
- If the user is saved in the database, the user with the user_id will be deleted and then, there will be a response that will be in the output, the response should be the name of the user_id which you passed followed by 'has been deleted', but if the user is not saved in the database, then 'Invalid Input Parameter' will be the output.


