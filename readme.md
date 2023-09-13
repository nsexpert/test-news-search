# Environment for running project.

-client
node 16.13.0

-server
python 3.9.0
pip 20.2.3

# What did I use to develop this project?

I have used some technologies to develop seamless, efficient and also user-friendly production.
For frontend, I have used vue3. And for efficient searching, I have implemented 'Debouncing Technology' by using custom vue3 directie(v-debounce). And I have used webpack to build the project.
And for backend, I have used news API (https://newsapi.org) for retriving news data that matches the keyword.
You can get the API from *newsapi.org* site easily.

# How to run the project?

1. Please clone the repository from the github

2. Then let's run the server first
    ==========> Server <===============
    Did you install python3.9.0
    if so, you can easily run the server by using *!run.bat* (It installs all the needed modules by using pip and then run the project automatically)

3. Then let's go on the client side.
    ===========> Client <==============
    - please install the node modules by using *npm i*
    - then you can run the vue project by running this command *npm run client*

4. That's it. Thank you.

# How to change the API KEY and the news source for searching?

You can change the API KEY and news source in server folder .env file. :)