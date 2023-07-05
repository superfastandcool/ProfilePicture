# Rose Graph Generation
A simple, albeit fairly complex mathematically, program used to generate a variety of graphs known as "rose curves".
![A blue rose curve.](https://avatars.githubusercontent.com/u/104604556?v=4)



## Using the program
To use this program, ensure Matplotlib and NumPy Python libraries are installed. Click [here](https://pypi.org/project/matplotlib/) to view installation instructions for Matplotlib and click [here](https://pypi.org/project/numpy/) for NumPy.

Once installed, change the value of $n$ to generate different graphs. I used $n = {4 \over 5}$ to create the rose curve shown.
This program was used to generate my profile picture.

## Developing the program
The formula for sketching the graph was based on the polar equation $r = \cos(n\theta)$. The equivalent parametric equations were used in the program:
$$x = \cos(n\theta) \times \cos(\theta)$$
$$y = \cos(n\theta) \times \sin(\theta)$$
