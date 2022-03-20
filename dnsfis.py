from turtle import distance
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import plotly.express as px
rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
data_rows = rows[1:]
mass_list=[]
radius_list=[]
gravity_list=[]
nearby_stars=[]
good_stars=[]
star_names=[]
distance_list=[]
for star in data_rows:
    mass=star[8]*1.989e+30
    distance =star[5]
    radius=star[9]*6.957e+8
    gravity=6.67430e-11*(mass/(radius*radius))
    mass_list.append(mass)
    radius_list.append(radius)
    gravity_list.append(gravity)
    if star[5] <= 100:
        nearby_stars.append(star)
        if gravity <350 and gravity>150:
            good_stars.append(star)
    star_names.append(star)

fig = px.bar(x=star, y=mass_list)
fig = px.bar(x=star, y=radius_list)
fig = px.bar(x=star, y=gravity_list)
fig = px.bar(x=star, y=distance_list)
fig.show()