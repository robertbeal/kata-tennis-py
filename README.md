A different approach and solution to the game of tennis. A commonly seen (and arguably unelegant, brittle) solution is storing players scores as integers, incrementing them and doing some sort of integer to score conversion. This solution goes in a very different direction. The basic concept is at any given point (ie '15-30') there are only two outcomes (ie '30-30' or '15-40') and that the game of tennis has a finite number of score permutations. Therefore it's simply a case of traversing the score "tree".

It's written using connascence as a tool for decoupling implementation/tests and reducing technical debt.

````
make build  # build the container
make test   # run the tests
make        # build, test
````
