## Solution Design: Learn Mandarin with Images Website

### HTML Files

1. `index.html`:
   - Serves as the homepage of the website.
   - Welcome message.
   - Navigation links to various Mandarin lessons and resources.
   - Images and videos to make the learning process more engaging.


2. `lessons.html`:
   - Contains different Mandarin lessons organized by levels (Beginner, Intermediate, Advanced).
   - Each lesson includes images, audio, and interactive exercises.


3. `resources.html`:
   - Offers additional learning materials like grammar guides, vocabulary lists, and cultural insights.
   - Links to language learning apps, podcasts, and online communities.


### Routes

1. `/`:
   - Maps to the `index.html` file.
   - Displays the homepage of the website.


2. `/lessons`:
   - Maps to the `lessons.html` file.
   - Displays a list of all Mandarin lessons available on the website.


3. `/lessons/<lesson_level>`:
   - Maps to the `lessons.html` file.
   - Dynamically generates the lessons page for a specific level (e.g., `/lessons/beginner`, `/lessons/intermediate`).


4. `/resources`:
   - Maps to the `resources.html` file.
   - Displays the page containing additional learning materials and resources.