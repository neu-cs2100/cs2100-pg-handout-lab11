This question is about the content of Homework 9. If you haven't done it yet, accept Homework 9 on Pawtograder and read its instructions (in README.md).

In Homework 9, we define the weight of the edge between two nodes as the geographical distance between the two stations.

What if we defined the edge weight some other way? For example, we could say, "the Fruitvale BART is 15 minutes from here," and that would be a meaningful weight.
In that case, we would be defining the edge weight as the number of minutes it takes to travel between the two nodes.

Let's discuss the pros and cons of various definitions of the edge weight.

Let's pretend that we are going to use these new edge weights to build a new MST, keeping the stations where they are, and replace the existing train tracks with the new tracks from the new MST.

### Practicality [3 points]

We could define the edge weight between two stations as the financial cost of
building the track between them (which is bigger if we have to dig a tunnel
underwater or through a mountain).

_Ethically, what are the pros and cons of using money as the edge weights to
build an MST to choose train tracks?_

### Privacy [3 points]

We could define the edge weight as 1/n, where n is the number of passengers who
regularly travel between the two stations. To count the number of passengers
who travel between two stations, we need to keep track of each passenger's
entrance and exit station. This would require asking the ticketing company
to give us the entrance and exit locations for each passenger.

_How could we protect riders' privacy while still using that data?_

### Fairness [3 points]

Traveling by public transportation costs different amounts of money, depending on
how far you're going. Additionally, passengers with low incomes can
receive discounted tickets.

What if we defined the edge weight between two stations as 1/n, where n
is the revenue from ticket sales from passengers travelling between
those two stations?

_How would you ensure that it still services all communities, including
those with less money?_

### Climate change [3 points]

We want to reduce traffic congestion and greenhouse gas emissions from cars
driving on the roads. Let's assume that car drivers will switch to public transportation if it
is more convenient than driving.

_What definition could we use for the edge weights such that the MST will
select a system of train tracks that would reduce the number of cars on the
road?_
