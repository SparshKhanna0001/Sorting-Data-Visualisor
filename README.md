# Challenge : To Create a Sorting Algorithm Visualisor w/o Prior Work Experience in GUI, Noob


```SECTION:-
    a. WHY
    b. How To Install
    c. App 
        i) Description
        ii) Gallery
    d. EXPERIENCE
        i) Approach
        ii) What Happened
        iii) INSIGHT Earned
    e. Links
```
## How To Install

### Just Install the executive:-
OR    
 Download this whole repo and do the compiling stuff urself!

## App

### Description:-
As said, it is very simple app. All you have to do is enter 5 numbers all less than ten in a text box.
Then Submit it and then it is will check whether it is correct or not, your input
Then Select the Type of Algorithm you want to execute and the Visualisation Begins.

### Gallery
 FOR VIDEO :- Navigate to Media Files Folder    

## Why?
Wanted to test would i be able to create an App *Peacefully* using AI (ChatGPT, Bard, Bing). So,as to Gain Insights about the future.

## EXPERIENCE

### Approach
* Use Already Developed Sorting Algorithms from GitHub [Initial Plan: To use those provided by WlliamFiset]
* Then Use a Java Based Module to create a GUI which will display the working of sorting algorithm via Bars moving.

### What Happened
* Used Bard to create an action plan
    1. He/or maybe it suggested libraries that weren't that beginner friendly but i was willing to learn them too.
    2. D3 was the one that i selected out of multiple options
        +Learned that it was JavaScript Based therefore had to get over JS too. No problem. 
        + But, D3 will create a web app.
            - Now it's a problem since i want a GUI based Solution
       _Failed!_ New Approach -> need of the hour
    3. Since, i m fluent in Python, therefore searched for Java To Python API.
        + The results weren't anything near satisfactory
    _Another Approach Required_
    4. ANOTHER APPROACH:- Learned that someone did created a forked version of the Algo Repo i wanted to use, so why use Java To Python API when you can do everything in Python. NICE MOVE
    5. Talked to Bard to Proivide correct python framework
        + Selected PyPlot at first
            - Web Based Solution; was willing to use despite this as Thought wud use Flask to display
            - But, it didn't provided that robust animation facility that i was looking for..!
            - Another Framework
        + Did Selected ALtair now since Bard explicitky stated that it has a SHIFT feature which is reqd for shifting of Bards. 
            - installed that too
            - And learnt that it doesn't again Offer the type of animations, i was looking for
            -_Plan Rejected_
        + About to use matplotlib but it seemed solving this way wud complicate it further therefore....
    6. Selected Turtle
        + Broke the problem into multiple parts
        + created code with the help of bard and ChatGPT
        + Everything was going great untill i had to implement the _Button Functionality_. 
        + Doing Buttons in tkinter is quite inefficient
        + So, shifted to Tkinter
    7. Tkinter
        + Learnt about it online websites and Bard too.
        + Used Bard extensively to create the app
        + Got a lot of errors and therefore frustation but there was visible more progress than other approaches.
            - That pack() and grid() did created a lot of hurdles
        + Tkinter App is ready now, now time for integrating it with the turtle components i created.
    8. Integration
        + Learned that it is better option to tailor my code for Tkinter then to integrate it.
        + Tailored it with the help of Bard and ChatGPT and Co-Pilot too
        Integration was an extremely horrible experience. Didn't liked it all.
        After more frustation and aggression, integration was done too.
    9. Integrating the Algos
        + This step although was the easiest one
        + Realised that the original Algorithms provided by the *Armin Zare Zadeh* needed a modification
            - Becoz i have to update the animation each time there is a change in the array structure
            - Asked ChatGPT to tailor the code, added callback therefore.
        + After modifying the code.
    10. Last Changes
        + Did a lot of testing and wasn't able to implement MergeSort and BucketSort correctly therefore deleted them from App
        + Added a simple and not so elegant menu (becoz both of the chatbots were suggesting wrong methods, therefore abandoned styling)
        + Tested Again, multiple times

    Completed.


### INSIGHT Earned
* I suffered a lot and honeslty this way of creating an app is not a good idea. It is better to learn stuff and plan urself then o completely rely on AI.
* AI Tools can only be used as a replacement to Interns and Junior Developers. Therefore in future the need for them will be eradicted.
* _LEARNING_ It is better to understand the documentation and Plan urself to completely rely on AI =, will save a lot of time.
* _HOW TO USE AI_:- Once through the theoretical part [done with the thought process] do use AI to tell it to create fucntions and then modify it based upon the understanding gained from the docs. Complelety relying on AI even if u r using it with critical thinking is not a good idea for now, untill it advances further.



## IMP LINKS:-
    1. ( Python Algorithms )[ https://github.com/akzare/Algorithms ]
    2. 
