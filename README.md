
## Spline drawer
In mathematics, a spline is a special function defined piecewise by polynomials ([read more](https://en.wikipedia.org/wiki/Spline_(mathematics))). <br />We need three parameter for drawing spline. t, c and k. like this image.

<p align="center">
<img src="./static/spline.svg" width="660" height="412" />
</p>


### Run
```
git clone https://github.com/mo1ein/spline-drawer-danaxa.git
cd spline-drawer-danaxa
pip install -r requirements.txt
python -m flask --reload
```

### API
```
localhost:5000/spline/
```

### Result
As you see in `test.py`, we have more x and y cordinates of points. After process data, you can see splines :)

<p align="center">
<img src="./static/out.jpg" width="500" height="380" />
</p>
