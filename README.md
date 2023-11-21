# Microservice
This is the repository that contains the files for the partner microservice

This is a Flask microservice that checks if a spell that a user enters is in the spell database. 

You may choose to implement the logic differently in you final implementation, but for demonstration purtposes,
I set this up so that you make a GET request to /check_spell that will return a JSON object True/False for the spell
you chose to check. The microservice will check the data base that you point to (in this case I just added a few
random spells to a dictionary). If the spell is indeed in the database, the client will recieve a JSON object containing
{"result": true} or {"result": false}. Using these JSON objects, your spell search app can implement other functions 
that can return the type of spell, what the spell does, and any other details you decide. 


UML Sequence

+------------------+        +-------------------+        +---------------------+
|     Client     |        | Flask Microservice|        | Spell Database/Set  |
+------------------+        +-------------------+        +---------------------+
        |                           |                             |
        |GET /check_spell?name=spell|                             |
        |-------------------------->|                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |                             |
        |                           |   Check if 'spell' exists    |
        |                           |--------------------------->|
        |                           |                             |
        |                           |      Return {"result": True}|
        |                           |<---------------------------|
        |   Receive {"result": True}|                             |
        |<--------------------------|                             |
