# [Problem 3: Targeted Ads](https://www.unb.ca/saintjohn/sase/_assets/documents/problems2019.pdf)

A major company would like to place advertisements at some public places, but they would like 
to put them where there will be enough of their targeted audience to see it. In order to 
estimate such targeted audience, they decide to do a quick survey on the street (to people 
passing by) at each of the locations they have in mind. The idea is that if there are enough 
people from their target audience (perfect cases or close enough), they will put an ad there.

The target audience is people in their 30s, spending 6 to 10 hours of screen time per week 
(inclusively), and owning a car. That would be the ideal audience (“perfect” cases). However, 
they would be content with the following cases (“close enough” cases):
- Persons in their 30s, with a car but with screen time either between 3 and 5 hours, or 
between 11 and 15 hours (inclusively)
- Persons with a car and with screen time between 6 and 10 hours, but in their 20s or in 
their 40s

Your program should count the number of people at each location, that match perfectly the 
target audience or that are close enough, and then decide whether each location is good or not 
based on given thresholds on those counts. 

The input starts with the 2 thresholds on the first line (2 positive integers). The first number is 
the minimum number of “perfect” cases we should have, and the second number is the 
minimum number of “perfect” cases + “close enough” cases we should have. Both thresholds 
should be met in order to consider this location a good one.

The second line of input indicates how many locations we have to handle. Then for each 
location, we start with the name of that location on one line, followed by the number of 
persons surveyed on the following line. Then for each person surveyed, we have the following 3 
pieces of information (all on one line, separated by spaces): age, number of hours of screen 
time, and “yes” or “no” indicating if the person owns a car or not.

The output should be, for each location: (1) the words “Good:” or “Not good:”; (2) the name of 
that location; (3) the number of “perfect” cases; and (4) the sum of the 2 counts (number of 
“perfect” and number of “close enough”). Note that the 2 numbers in the output are the ones 
that we compare to the thresholds provided in the first line of input.

## Sample Input 1
```
3 5
2
mall
9
25 6 yes
31 8 yes
33 10 no
40 4 yes
36 7 yes
39 9 yes
41 6 yes
21 8 no
32 15 yes
uptown
6
35 6 yes
34 7 no
31 8 yes
19 9 yes
38 7 yes
32 13 no
```

## Sample Output 1
```
Good: mall 3 6
Not good: uptown 3 3
```
