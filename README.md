# All You Can Eat

- **All You Can Eat** is a python terminal program that runs on the Code Institute mock terminal on Heroku. 

- The program was inspired by a real life argument that I had with my closest friends. We met at University in a medium-sized town in Sweden(Helsingborg) and one evening not long ago we couldn't agree on which fast-food restaurant in our vicinity was actually the best. 

- So I made a survey, with 7 of the most popular fast-food joints that we used to frequent and asked them to fill it out and give ratings in five categories. Those being: Taste, Care (hospitality) Cleanliness, Price and Speed. This was the main purpose first and foremost - to end the debate through calculating an average score in each category - and then a total average score to display neatly and with an easy user interface. 

<img> ![A screenshot of a part of the game.](assets/images/responsivity.png)

## Features
---
### Existing Features

### Data Collection
 - Collect and maintain data. Uses google.sheets to gather information and collects name and e-mail for google.sheets aswell. 

### Validation
 - Shuts down if player refuses to give proper name values
 - Gives feedback if numerical inputs aren't within the scope.
 - Validates through print-messages whenever you choose something and provides several options in most cases.

### Calculation
 - Calculates the values of the columns for each restaurant. 
 - Calculates total averages. 

### Play Forever
 - The program is looped and the only time you can exit is:
   - By not giving correct name values.
   - User opts to quit. 

### Future Features
 - A separate list where the total scores of all restaurants can be viewed
 - Update autonomously and through any length and categories.
 - More cities and restaurants.

<img> ![A screenshot showing the red/orange navigation menu of the webpage](assets/images/nav-bar-jasmin.png)

## Data Model / Methods / Libraries

 - All You Can Eat hasn't imported any extensive data models or classes, but uses classes like: list & map aswell as systemExit to terminate the game. 
 - Methods that are in use are to help manage lists like: append, get.all.values and then also isAlpha for the name input fields. 
 - The program however uses tabular as a tool to help print a finer, more structured terminal and makes it easier get keys for headers. During my project I have stumbled upon Panda which I probably will look deeper into the next time I work with python. 
 
<img> ![A screenshot showing the Peptalk/header-section of the page](assets/images/peptalk3.png)

## Testing
- I have manually tested the project
  - Passed the code through...
  - Given invalid inputs at different stages.
  - Ran the program over 500 recorded times during project to try all validations
  and made all the calculations manually aswell. 

<img> ![A screenshot showing the guide-section of the page](assets/images/guide-jasmin.png)

## Bugs

### Solved Bugs
  
  - The biggest challenge was creating the for loop used to calculate averages using flow control and encoding the classes and using elements to do the correct math. No large bugs or errors here, just tough logic.  

  - The program had a "bug" where even if you would use the input to go back and view more restaurants the functions would only print the next page and the content was not interactive. This was solved through looping all main functions (except name) and then having a different loop 'restart' the program.

### Remaining bugs

  - My scope was originally 7 restaurants in one city, but nearing the end I added some extra cities and restaurants at first as placeholder to give the program some more weight, however these do not work as intended. Towards the end after I had polished the code I still wanted to make atleast one more city interactive but due to my inital scope I had not planned ahead of time to a future where the program would expand. The variable 'city_str' became a variable for too much data which made it too time-consuming and difficult to edit by the end. In retrospect I should have better separated variables and made smaller functions instead of trying to do too much at once.  


 ## Credits
---
 ### Content

 ### Guides & Troubleshooting

 ### Tabulate

- [Pypi](https://pypi.org/project/tabulate/) 

 ### Round

- [Bobbyhadz](https://bobbyhadz.com/blog/python-round-number-to-1-decimal#:~:text=Use%20the%20round()%20function,precision%20after%20the%20decimal%20point.) 

### Try:Except:Finally & SysExit

- [W3Schools](https://www.w3schools.com/python/python_try_except.asp)
- [Stackoverflow](https://stackoverflow.com/questions/25905923/python-sys-exit-not-working-in-try)
- [CSS Deck](https://cssdeck.com/blog/how-to-make-a-sticky-header-step-by-step/) 

### About Exiting Loops

- [Quora](https://www.quora.com/Can-a-break-statement-be-used-to-exit-a-while-loop-in-Python)
- [Maschituts](https://maschituts.com/exit-while-loops-in-python/)

### Iteration
- Code Institute Course Material
- [Geeksforgeeks](https://www.geeksforgeeks.org/iterate-over-a-list-in-python/)