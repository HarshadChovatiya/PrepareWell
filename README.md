# PrepareWell
Command line tool developed using python to test user's reading, listening and writing skill for english language

### Technology in use
    python (version 3 preferable)

### Libraries
    Speech recognition - for recognizing voice
    Gtts - google text to speech
    Playsound - for playing audio
    Difflib - to compare two paragraphs
    Colorama - for producing colored terminal text
    Wikipedia-api - to get summary on any topic from wikipedia
    Matplotlib - for graph generation
    Pyperclip - to handle copy and paste


### Functionalities
    - User can test their reading, listening and writing skill for english language
    - Each time a random wiki-pedia paragraph will be given to the user
    - User can see the performance in a graph form (need to give atleast two test to see performance)

### Spotlights
    It’s dynamic
      Each and  every  time user will get a randomly fetched paragraph which contains summary for
      the particular topic in the wikipedia
    Caching mechanism
      From the set of topics whenever it’s time to fetch the paragraph program will look inside
      a file to check that whether this topic is previously fetched or not, if it is then no need
      to do the api call , just use that paragraph. If not then fetch and store it in the file for the later use.
      Once the user exit stored cache will be deleted automatically.

#### Side Note
    colored printing statement may not work in some terminal (use vscode's terminal for better experience)
