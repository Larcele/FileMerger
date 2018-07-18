This all started when I was developing a web application.

For the sake of maintainability I kept multiple .css files for styling. Ultimately, I wanted to use only a single merged one from all the others, in order to limit the amount of Http requests the site would need to do (to increase performance), while still keeping the files separate for better development. 
I was never really happy with the online tools which did this, with all their clicking and long procedures.

And that's why this was created.

This is a simple python script, along with a config file (source.txt). The file consists of two lines;
The first one defines the location of all the .css files you wish to merge
The second one defines the location where you want your merged file to be created.

Then, you run it, and get it merged. No clicking, long procedures, and frustration with the online solutions.
