# ringify
Python script for galaxy density profiling!

## Are you tired of not knowing the mass distribution of your galaxy?
Well, fear no more! Ringify can spot the center of your galaxy, then slice successive rings from it, then checking they're density!

###### There's a lot of work left, and i may stop updating it at any time (it's just the first step to a much much greater work on galactic simulations).


## HOW TO RUN IT:
```
python3 ringify.py <insert_your_snapshot>
```
###### In case you don't have any snapshots, the file "gal_test" is the one i've been using for testing purposes.

## WHAT SHOULD HAPPEN?
> The mass density of each ring should appear on your terminal, just as a cute graphic pops up and gets saved as a png!


## WHAT DO YOU NEED TO RUN IT:

> python libraries:
  - numpy
  - matplotlib
  - unsio
  
  
In case you never heard of this type of simulations, there's a fantastic guide made by Rubens Machado, the lead professor from the UTFPR Extragalactic Research Group. Here's the link: http://paginapessoal.utfpr.edu.br/rubensmachado/outros-1/Nbody-tutorial-2022.pdf

## Future Changes:

- (MAYBE) The number of rings should be an argument of the script. Currently, to change it, you need to do it manually in the code
- The graphic needs some work (better scaling, axis names, correct ticks, etc)
- (MAYBE) A second, more "visual", type of graphic



###### Thanks for reading, hope you like it!
#### v.f.f
