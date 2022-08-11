
## spline drawer
Draw spline in image with given points P. `P(t, c, k)` t is c and k is degree.

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
<img src="./upload/out.jpg" width="660" height="412" />
</p>
