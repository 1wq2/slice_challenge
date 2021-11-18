# Slice Code Challenge

## Introduction

Pizzabot - bot for pizza delivery. Given addresses on a grid provide Pizzabot with instructions on how to 
deliver pizzas to all mentioned locations. An instruction is one of:
```
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza
```

## Solution's peculiarities

* ```a list of points representing houses in need of pizza delivery```

I decided to take this requirement literally: here we are talking about a list of houses, not the amount of pizzas
to be delivered. From this requirement, we cannot determine the amount of pizzas that will be delivered, but only 
the location of the houses. But, I might add, that is an uneasy assumption for me.

If we encounter the same point twice, one immediately after another, we will make only one delivery to this 
location. Again, "delivery" can mean multiple customers of this house. 

A real-world example of how this mistake(duplicate location) could've happened. We'll have a list of pizza orders, 
from the "orders" list we are populating/optimizing "destination" lists. But for some 
reason(such as an error in the processing of the user's input) our optimization algorithm gave us a slightly wrong list.


* I wasn't implementing the shortest distance algorithm, since this was implicitly mentioned as unnecessary. 
Basically, the bot will be moving on the X-axis first, then on the Y. That's it. 



## Prerequisites

* Python and pip. Should be already installed if you are using Linux/Ubuntu. Tested on Ubuntu 20.04
* pytest. You can install pytest with this command ```pip install -U pytest```

## Running
Open project's folder in a terminal and run a command like this:

```sh
$ python3 ./pizzaBot.py "5x5 (1, 3) (4, 4)" 
```

Sample output: 

```ENNNDEEEND```

The parser that handles user data is quite flexible, so it's completely fine to run this command:

```sh
$ python3 ./pizzabot.py "5 x  5 (1, 3  4, 4" 
```
Basically, don't forget to use '(' as a delimiter for the grid and coords data, and parser will handle the rest.

It ain't argparse, but still better than bare default. 

This and other input examples can be checked in the ```test_pizzabot.py``` file.

To run those tests just type 
```sh
$ pytest 
``` 
command in a terminal and hit ```Enter```. 
 