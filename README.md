First off, I'm not sure what I was thinking trying this out, however, I knew that I was not going to survive doing this manually with multiple cut and paste files, and manually entering 500+ coard in Anki, for both front and back. I think I made about 60 manually and knew that this was not going to scale well.

Second, I know I could probably use several tools to some how make this work, but did I have the time to do it, no really.

So, I decided to go to ChatGPT and see what it could do. Turns out it worked fairly well.

Thniking about what I needed to do, and breaking it up into 3 phases seemed like the easiest way for me to think about how I could devide up this work and make it in smaller chunk which were part of an interative process. One, this would keep the logic compartmentalized, and two I could trouble shoot sections if something went wrong.

There was a bit of manual pre-processing I did to remove some text, but I could have built this out too, I just wasn't thinking about it at the time.

Also, looking at the Anki site and a couple of search engine searches I couldn't find an Anki deck for this version 2024-2028, so I needed to make one.

I experimented with Anki making some card, figuring out how I wanted it to work, as a simple front/back , with the back having the soame contents as the from but the answerr highlighted in some way.


Starting file is a text file which is basically a copy/paste from the ARRL/VEC Office-style .docx. 

Preprossessing = 
  - Take the doc file and manuall highlight the Question Pool and paste to a text file.
  - Manuall remove som eof the refernces to the FCC regulations in brackets next to the answer.
  - Removed some blank lines (not sure this was needed)

Phase one:
  - Interpret the text file and put the lines of each question into string variables for easy manipulation.
  - Set up the format of the Question and multiple choice answers for the front of the card, followed by the same on the back of the card with the answer key.

Phase two:
  - Basically convert that newly processed file from phase one to wrap HTML tags around each line.
  - Write the correct HTML higlighint or dimming rather for the incorrect answers on the card.

Phase three:
  - Write the answers to csv format in two columns cels A1:B1, A2:B2, A3:B3, etc...



