# Dokumentation
### Gruppe Streckung und Stauchung
### Seminar Visuelle Wahrnehmung beim Menschen und Bildqualität

# Motivation

Die Idee hatten wir, weil ein Mitglied unserer Gruppe ein stark verzerrtes Foto im Studierendenausweis hatte und wir uns fragten, wie sich Verzerrung auf die menschliche Wahrnehmung auswirkt. Etwas Brainstorming kombiniert mit der Niedlichkeit von Hunden und Katzen brachte uns schließlich dazu, untersuchen zu wollen, ob Menschen Bildverzerrung bei anderen Menschen schneller erkennen als bei Hunden und Katzen. Damit waren wir also bei zwei Fragestellungen und Hypothesen:

"Können Menschen Stauchungen deutlicher erkennen als Streckungen?"
und unsere Hypothese:
"Wenn Menschen empfindlicher für Stauchungen als für Streckungen in Bildern von Gesichtern sind, dann erkennen sie die gestauchten Bilder deutlicher."

sowie
"Sind Menschen empfindlicher für Bildverzerrungen in menschlichen Gesichtern als in Gesichtern anderer Spezies wie beispielsweise Hunde oder Katzen?"
und die dazugehörige Hypothese:
"Wenn Menschen empfindlicher für Verzerrungen in Bildern von menschlichen Gesichtern sind, dann sollten sie bei gleichem Verzerrungsgrad, die Verzerrung eher in menschlichen als tierischen Gesichtern erkennen."

# Sammeln und Aufbereiten der Bilder

Wir entschieden uns, Bilder von eigenen Haustieren sowie denen aus Freundes- und Familienkreis zu sammeln und bei den Menschen auf Bilder von Prominenten zurückzugreifen. Nach dem Sammeln der Bilder standen wir allerdings vor dem Problem, das ein einfaches Verzerren der Bilder leicht an der unterschiedlichen Länge der Bilder zu erkennen wäre. Deshalb haben wir alle Gesichter der Versuchsobjekte per Hand einzeln in einem Bildbearbeitungsprogramm ausgeschnitten, bevor wir die so vorbereiteten Bilder verzerrten.

# Skript zur Verzerrung der Input Bilder

Unser Skript zur Verzerrung der Bilder hat sich im Laufe des Projektes verändert. In der ersten Fassung war der Verzerrungsgrad für jedes einzelne Bild komplett zufällig, wodurch wir nicht sicherstellen konnten, dass gestauchte und gestreckte Bilder, beziehungsweise Bilder von Menschen und Haustieren gleich stark verzerrt waren. Das hätte den Vergleich verfälscht, also musste ein neues Skript her. 

In dieser Version werden die Verzerrungsstufen alle der Reihe nach auf die Bilder angewendet, um eine gleichmäßige Verteilung zu gewährleisten.


```python
import cv2
import glob
import copy
import os
import csv
import random

from IPython.display import Image

### global variables
path_parent_folder = os.path.dirname(os.getcwd())
print(path_parent_folder)
path_input_files = path_parent_folder +"/input/"
path_input_pets = path_input_files + "pets/"
path_input_humans = path_input_files + "humans/"
path_output_files = path_parent_folder + "/output/"
file_type = ["/*.jpg", "/*.csv", "/*.png"]
```

    /home/jan/Documents/VW



```python
### fetch all images in folder and save in list
data_path_humans = glob.glob(path_input_humans + file_type[0])
human_image_list = []
for img in data_path_humans:
    images = cv2.imread(img)
    human_image_list.append(images)

data_path_pets = glob.glob(path_input_pets + file_type[0])
pet_image_list = []
for img in data_path_pets:
    images = cv2.imread(img)
    pet_image_list.append(images)
```


```python
### copy list of images to process further
human_streched_image_list = copy.deepcopy(human_image_list)
human_compressed_image_list = copy.deepcopy(human_image_list)
pet_streched_image_list = copy.deepcopy(pet_image_list)
pet_compressed_image_list = copy.deepcopy(pet_image_list)
```


```python
def transformImageVertically(ListOfImages, number_from, number_to, number_step, img_type):
    count_number = 1
    scale_percent = number_from
    
    for item in ListOfImages:
        # needed to call fkt. without distortion
        if(number_step != 0):
            # added to ensure all distortion rates are applied
            if(scale_percent < number_to and (count_number != 1) and (count_number % 2 == 1)):
                scale_percent += number_step
        else:
            scale_percent = 100
            
        # keep default img width
        original_width = item.shape[1]
        
        # manipulate height by % in given range
        new_height = int(item.shape[0] * scale_percent / 100)
        
        # saves height and width
        dim_size = (original_width, new_height)
        
        # apply distortion
        vScaled_img = cv2.resize(item, dim_size, interpolation=cv2.INTER_AREA)
        
        # resizes image to 10cm height
        if(scale_percent == 150):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /1.5), fy=(1 /1.5))
        elif(scale_percent == 140):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /1.4), fy=(1 /1.4))
        elif(scale_percent == 130):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /1.3), fy=(1 /1.3))
        elif(scale_percent == 120):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /1.2), fy=(1 /1.2))
        elif(scale_percent == 110):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /1.1), fy=(1 /1.1))
        elif(scale_percent == 50):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /0.5), fy=(1 /0.5))
        elif(scale_percent == 60):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /0.6), fy=(1 /0.6))
        elif(scale_percent == 70):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /0.7), fy=(1 /0.7))
        elif(scale_percent == 80):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /0.8), fy=(1 /0.8))
        elif(scale_percent == 90):
            vScaled_img = cv2.resize(vScaled_img, (0, 0), fx=(1 /0.9), fy=(1 /0.9))
       
        # save files in right format
        cv2.imwrite(path_output_files + '/{}{}_{}.png'.format(img_type, count_number, scale_percent), vScaled_img)
        count_number += 1
```

Die Funktion wurde für die Menschen und Haustierbilder je drei mal ausgeführt, um gestreckte, gestauchte und unveränderte Bilder mit Dateinamen im richtigen Format zu jedem Objekt zu erzeugen.


```python
### create image files for humans (set correct input path first!)
# calls function with params to stretch images
transformImageVertically(human_streched_image_list, 110, 150, 10, "human") 
# calls function with params to compress images
transformImageVertically(human_compressed_image_list, 50, 90, 10, "human")
# calls function with params zero to only change file name without distortion
transformImageVertically(human_image_list, 0, 0, 0, "human")
```


```python
### create image files for pets same way
transformImageVertically(pet_streched_image_list, 110, 150, 10, "pet") # 110 -150
transformImageVertically(pet_compressed_image_list, 50, 90, 10, "pet") # 50 - 90
transformImageVertically(pet_image_list, 0, 0, 0, "pet")
```


```python
### write csv file with all file names
file_name_list = []

# needed for right format
list_of_lists = []

# set folder to output path
data_path2 = glob.glob(path_output_files + file_type[2])

# select all file names in folder and save in list
for i in range(0,len(data_path2), 1):
    file_name_list.append(os.path.basename(data_path2[i]))
    
# needed to apply experiment script
header = ["test_image"]

# needed for right format
for item in range(0,len(file_name_list), 1):
    list_of_lists.append([file_name_list[item]])

# creates csv file with all image names listed in one coloumn
with open(path_output_files + 'scaledImages.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(list_of_lists)
```

Danach werden die Einträge noch mit dem folgenden Script zufällig angeordnet. Um zu vermeiden, dass im Experiment Bilder des gleichen Gesichts direkt aufeinander folgten, haben wir diese danach noch per Hand auseinander geschoben.


```python
def randomize_pictures(path):
    output="test,image\n"
    lineList = []
    with open(path) as f:
        for line in f:
            if line == "test,image\n":
                continue
            lineList.append(line)
    random.shuffle(lineList)
    for line in lineList:
        output += line
    f= open(path,"w")
    f.write(output)
        

randomize_pictures(path_output_files + 'scaledImages.csv')
```

# Versuchsaufbau

Im Versuch wurden die Gesichter in zufälliger Reihenfolge auf weißem Hintergrund mit der Frage präsentiert, ob eine Verzerrung vorliegt. Die Antwort wurde von einer Begleitperson, die von uns gestellt wurde, über Tastendruck eingegeben. Jedes Gesicht wurde dabei drei mal in zufälliger Reihenfolge gezeigt: Einmal gestaucht, einmal gestreckt und einmal unverändert.

Das python script dazu ist im output Ordner als rating_experiment_single.py zu finden.

# Aufbereitung der CSV mit den Ergebnis Daten

Hinterher haben wir die Daten mittels command line Befehl: <*csv newMergedFile.cvs> in eine Tabelle zusammengetragen und die Informationen Bildtitel und Verzerrung voneinander getrennt in verschiedenen Spalten dargestellt.

Damit die Daten sinnvoll ausgewertet werden konnten, wurden entsprechende Header gesetzt und überflüssige Zeichen entfernt.


```python
def format(path):
    output=""
    with open(path) as f:
        for line in f:
            if not line == "\n":
                lineArray = line.split(",")
                if lineArray[0] == "test_image":
                    lineArray.insert(1,"distortion")
                    line = ",".join(lineArray)
                else:
                    objectArray = lineArray[0].split("_")
                    distortion = objectArray[-1].replace("%.png","")
                    lineArray.insert(1,distortion)
                    objectArray.pop()
                    lineArray[0] = "_".join(objectArray)
                    line = ",".join(lineArray)
                output += line
    output.rstrip()
    f= open(path,"w")
    f.write(output)

format(path_output_files + 'design_rating_single_results.csv')
```

# Datenauswertung


```python
import pandas as pd   # module to work with data in DataFrames.
import seaborn as sns  # module to plot DataFrames in an easy way
import matplotlib.pyplot as plt
import numpy as np
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    /home/jan/Documents/VW/code/Dokumentation_Seminar_IQP.ipynb Cell 26' in <cell line: 2>()
          <a href='vscode-notebook-cell:/home/jan/Documents/VW/code/Dokumentation_Seminar_IQP.ipynb#ch0000025?line=0'>1</a> import pandas as pd   # module to work with data in DataFrames.
    ----> <a href='vscode-notebook-cell:/home/jan/Documents/VW/code/Dokumentation_Seminar_IQP.ipynb#ch0000025?line=1'>2</a> import seaborn as sns  # module to plot DataFrames in an easy way
          <a href='vscode-notebook-cell:/home/jan/Documents/VW/code/Dokumentation_Seminar_IQP.ipynb#ch0000025?line=2'>3</a> import matplotlib.pyplot as plt
          <a href='vscode-notebook-cell:/home/jan/Documents/VW/code/Dokumentation_Seminar_IQP.ipynb#ch0000025?line=3'>4</a> import numpy as np


    File ~/.local/lib/python3.8/site-packages/seaborn/__init__.py:2, in <module>
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/__init__.py?line=0'>1</a> # Import seaborn objects
    ----> <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/__init__.py?line=1'>2</a> from .rcmod import *  # noqa: F401,F403
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/__init__.py?line=2'>3</a> from .utils import *  # noqa: F401,F403
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/__init__.py?line=3'>4</a> from .palettes import *  # noqa: F401,F403


    File ~/.local/lib/python3.8/site-packages/seaborn/rcmod.py:5, in <module>
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/rcmod.py?line=2'>3</a> import functools
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/rcmod.py?line=3'>4</a> from distutils.version import LooseVersion
    ----> <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/rcmod.py?line=4'>5</a> import matplotlib as mpl
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/rcmod.py?line=5'>6</a> from cycler import cycler
          <a href='file:///home/jan/.local/lib/python3.8/site-packages/seaborn/rcmod.py?line=6'>7</a> from . import palettes


    File ~/.local/lib/python3.8/site-packages/matplotlib/__init__.py:109, in <module>
        <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=104'>105</a> from packaging.version import parse as parse_version
        <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=106'>107</a> # cbook must import matplotlib only within function
        <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=107'>108</a> # definitions, so it is safe to import from it here.
    --> <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=108'>109</a> from . import _api, _version, cbook, docstring, rcsetup
        <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=109'>110</a> from matplotlib.cbook import MatplotlibDeprecationWarning, sanitize_sequence
        <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/__init__.py?line=110'>111</a> from matplotlib.cbook import mplDeprecation  # deprecated


    File ~/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py:27, in <module>
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py?line=24'>25</a> from matplotlib import _api, cbook
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py?line=25'>26</a> from matplotlib.cbook import ls_mapper
    ---> <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py?line=26'>27</a> from matplotlib.colors import Colormap, is_color_like
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py?line=27'>28</a> from matplotlib.fontconfig_pattern import parse_fontconfig_pattern
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/rcsetup.py?line=28'>29</a> from matplotlib._enums import JoinStyle, CapStyle


    File ~/.local/lib/python3.8/site-packages/matplotlib/colors.py:51, in <module>
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/colors.py?line=48'>49</a> from numbers import Number
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/colors.py?line=49'>50</a> import re
    ---> <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/colors.py?line=50'>51</a> from PIL import Image
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/colors.py?line=51'>52</a> from PIL.PngImagePlugin import PngInfo
         <a href='file:///home/jan/.local/lib/python3.8/site-packages/matplotlib/colors.py?line=53'>54</a> import matplotlib as mpl


    ModuleNotFoundError: No module named 'PIL'



```python
sns.set_context('talk') 
```


```python
df = pd.read_csv(path_output_files + 'design_rating_single_results.csv')
```

# Datenaufbereitung und -überprüfung

Hier haben wir unsere gesammelten Daten zusammengetragen, um sie auf Fehler zu überprüfen


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_image</th>
      <th>response</th>
      <th>resptime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pet_4_120%.png</td>
      <td>1</td>
      <td>2.797793</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pet_6_100%.png</td>
      <td>0</td>
      <td>0.441570</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pet_1_50%.png</td>
      <td>0</td>
      <td>2.870934</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pet_4_60%.png</td>
      <td>0</td>
      <td>0.671194</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pet_10_100%.png</td>
      <td>0</td>
      <td>0.582222</td>
    </tr>
    <tr>
      <th>5</th>
      <td>human_5_70%.png</td>
      <td>0</td>
      <td>0.549280</td>
    </tr>
    <tr>
      <th>6</th>
      <td>human_6_100%.png</td>
      <td>0</td>
      <td>0.440528</td>
    </tr>
    <tr>
      <th>7</th>
      <td>human_2_100%.png</td>
      <td>0</td>
      <td>0.344681</td>
    </tr>
    <tr>
      <th>8</th>
      <td>pet_2_110%.png</td>
      <td>0</td>
      <td>0.377459</td>
    </tr>
    <tr>
      <th>9</th>
      <td>human_6_130%.png</td>
      <td>0</td>
      <td>0.328459</td>
    </tr>
    <tr>
      <th>10</th>
      <td>human_6_70%.png</td>
      <td>0</td>
      <td>0.295299</td>
    </tr>
    <tr>
      <th>11</th>
      <td>human_9_150%.png</td>
      <td>0</td>
      <td>0.312662</td>
    </tr>
    <tr>
      <th>12</th>
      <td>human_2_50%.png</td>
      <td>0</td>
      <td>0.245580</td>
    </tr>
    <tr>
      <th>13</th>
      <td>pet_7_100%.png</td>
      <td>0</td>
      <td>0.325179</td>
    </tr>
    <tr>
      <th>14</th>
      <td>human_7_140%.png</td>
      <td>0</td>
      <td>0.264291</td>
    </tr>
    <tr>
      <th>15</th>
      <td>human_7_100%.png</td>
      <td>0</td>
      <td>0.290106</td>
    </tr>
    <tr>
      <th>16</th>
      <td>human_10_90%.png</td>
      <td>0</td>
      <td>0.366077</td>
    </tr>
    <tr>
      <th>17</th>
      <td>pet_2_100%.png</td>
      <td>0</td>
      <td>0.406422</td>
    </tr>
    <tr>
      <th>18</th>
      <td>pet_5_130%.png</td>
      <td>0</td>
      <td>0.302926</td>
    </tr>
    <tr>
      <th>19</th>
      <td>human_5_130%.png</td>
      <td>0</td>
      <td>0.355319</td>
    </tr>
    <tr>
      <th>20</th>
      <td>human_8_100%.png</td>
      <td>0</td>
      <td>0.327620</td>
    </tr>
    <tr>
      <th>21</th>
      <td>pet_2_50%.png</td>
      <td>0</td>
      <td>0.351997</td>
    </tr>
    <tr>
      <th>22</th>
      <td>pet_3_60%.png</td>
      <td>0</td>
      <td>2.392761</td>
    </tr>
    <tr>
      <th>23</th>
      <td>human_9_100%.png</td>
      <td>0</td>
      <td>1.466001</td>
    </tr>
    <tr>
      <th>24</th>
      <td>human_4_60%.png</td>
      <td>0</td>
      <td>0.436620</td>
    </tr>
    <tr>
      <th>25</th>
      <td>human_1_100%.png</td>
      <td>0</td>
      <td>0.362253</td>
    </tr>
    <tr>
      <th>26</th>
      <td>human_2_110%.png</td>
      <td>0</td>
      <td>0.327447</td>
    </tr>
    <tr>
      <th>27</th>
      <td>pet_9_100%.png</td>
      <td>0</td>
      <td>0.533157</td>
    </tr>
    <tr>
      <th>28</th>
      <td>pet_10_150%.png</td>
      <td>0</td>
      <td>0.386300</td>
    </tr>
    <tr>
      <th>29</th>
      <td>pet_4_100%.png</td>
      <td>0</td>
      <td>0.446483</td>
    </tr>
    <tr>
      <th>30</th>
      <td>pet_3_120%.png</td>
      <td>0</td>
      <td>0.384932</td>
    </tr>
    <tr>
      <th>31</th>
      <td>pet_6_130%.png</td>
      <td>0</td>
      <td>0.449964</td>
    </tr>
    <tr>
      <th>32</th>
      <td>human_4_120%.png</td>
      <td>0</td>
      <td>0.457916</td>
    </tr>
    <tr>
      <th>33</th>
      <td>human_7_80%.png</td>
      <td>0</td>
      <td>0.510434</td>
    </tr>
    <tr>
      <th>34</th>
      <td>pet_8_140%.png</td>
      <td>0</td>
      <td>0.480026</td>
    </tr>
    <tr>
      <th>35</th>
      <td>human_1_50%.png</td>
      <td>0</td>
      <td>0.581321</td>
    </tr>
    <tr>
      <th>36</th>
      <td>pet_7_80%.png</td>
      <td>0</td>
      <td>0.518403</td>
    </tr>
    <tr>
      <th>37</th>
      <td>human_10_100%.png</td>
      <td>0</td>
      <td>0.585734</td>
    </tr>
    <tr>
      <th>38</th>
      <td>human_10_150%.png</td>
      <td>0</td>
      <td>0.349939</td>
    </tr>
    <tr>
      <th>39</th>
      <td>human_8_80%.png</td>
      <td>0</td>
      <td>0.539538</td>
    </tr>
    <tr>
      <th>40</th>
      <td>pet_10_90%.png</td>
      <td>0</td>
      <td>0.597935</td>
    </tr>
    <tr>
      <th>41</th>
      <td>human_5_100%.png</td>
      <td>0</td>
      <td>0.410473</td>
    </tr>
    <tr>
      <th>42</th>
      <td>human_9_90%.png</td>
      <td>0</td>
      <td>0.374565</td>
    </tr>
    <tr>
      <th>43</th>
      <td>pet_5_70%.png</td>
      <td>0</td>
      <td>0.637672</td>
    </tr>
    <tr>
      <th>44</th>
      <td>pet_8_80%.png</td>
      <td>0</td>
      <td>0.620025</td>
    </tr>
    <tr>
      <th>45</th>
      <td>pet_1_110%.png</td>
      <td>0</td>
      <td>0.895272</td>
    </tr>
    <tr>
      <th>46</th>
      <td>human_8_140%.png</td>
      <td>0</td>
      <td>0.792206</td>
    </tr>
    <tr>
      <th>47</th>
      <td>human_1_110%.png</td>
      <td>0</td>
      <td>0.448823</td>
    </tr>
    <tr>
      <th>48</th>
      <td>human_3_100%.png</td>
      <td>0</td>
      <td>0.442997</td>
    </tr>
    <tr>
      <th>49</th>
      <td>human_3_60%.png</td>
      <td>0</td>
      <td>0.346176</td>
    </tr>
    <tr>
      <th>50</th>
      <td>pet_9_90%.png</td>
      <td>0</td>
      <td>0.603589</td>
    </tr>
    <tr>
      <th>51</th>
      <td>pet_9_150%.png</td>
      <td>0</td>
      <td>0.667076</td>
    </tr>
    <tr>
      <th>52</th>
      <td>pet_3_100%.png</td>
      <td>0</td>
      <td>0.485343</td>
    </tr>
    <tr>
      <th>53</th>
      <td>human_3_120%.png</td>
      <td>0</td>
      <td>0.620716</td>
    </tr>
    <tr>
      <th>54</th>
      <td>pet_6_70%.png</td>
      <td>0</td>
      <td>0.780943</td>
    </tr>
    <tr>
      <th>55</th>
      <td>pet_8_100%.png</td>
      <td>0</td>
      <td>2.365931</td>
    </tr>
    <tr>
      <th>56</th>
      <td>pet_7_140%.png</td>
      <td>0</td>
      <td>3.098895</td>
    </tr>
    <tr>
      <th>57</th>
      <td>human_4_100%.png</td>
      <td>0</td>
      <td>1.399019</td>
    </tr>
    <tr>
      <th>58</th>
      <td>pet_1_100%.png</td>
      <td>0</td>
      <td>0.428919</td>
    </tr>
    <tr>
      <th>59</th>
      <td>pet_5_100%.png</td>
      <td>0</td>
      <td>0.383117</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['category'] = df['image'].astype(str).str[0]
df
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3621, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3619'>3620</a> try:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:136, in pandas._libs.index.IndexEngine.get_loc()


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:163, in pandas._libs.index.IndexEngine.get_loc()


    File pandas/_libs/hashtable_class_helper.pxi:5198, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    File pandas/_libs/hashtable_class_helper.pxi:5206, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'image'

    
    The above exception was the direct cause of the following exception:


    KeyError                                  Traceback (most recent call last)

    /home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb Cell 33' in <cell line: 1>()
    ----> <a href='vscode-notebook-cell:/home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb#ch0000030?line=0'>1</a> df['category'] = df['image'].astype(str).str[0]
          <a href='vscode-notebook-cell:/home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb#ch0000030?line=1'>2</a> df


    File ~/.local/lib/python3.8/site-packages/pandas/core/frame.py:3505, in DataFrame.__getitem__(self, key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3502'>3503</a> if self.columns.nlevels > 1:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3503'>3504</a>     return self._getitem_multilevel(key)
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3504'>3505</a> indexer = self.columns.get_loc(key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3505'>3506</a> if is_integer(indexer):
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3506'>3507</a>     indexer = [indexer]


    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3623, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3622'>3623</a>     raise KeyError(key) from err
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3623'>3624</a> except TypeError:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3624'>3625</a>     # If we have a listlike key, _check_indexing_error will raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3625'>3626</a>     #  InvalidIndexError. Otherwise we fall through and re-raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3626'>3627</a>     #  the TypeError.
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3627'>3628</a>     self._check_indexing_error(key)


    KeyError: 'image'



```python
#df.drop(['resptime'],axis=1,inplace=True)
```


```python
df['image'].unique()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3621, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3619'>3620</a> try:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:136, in pandas._libs.index.IndexEngine.get_loc()


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:163, in pandas._libs.index.IndexEngine.get_loc()


    File pandas/_libs/hashtable_class_helper.pxi:5198, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    File pandas/_libs/hashtable_class_helper.pxi:5206, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'image'

    
    The above exception was the direct cause of the following exception:


    KeyError                                  Traceback (most recent call last)

    /home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb Cell 35' in <cell line: 1>()
    ----> <a href='vscode-notebook-cell:/home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb#ch0000032?line=0'>1</a> df['image'].unique()


    File ~/.local/lib/python3.8/site-packages/pandas/core/frame.py:3505, in DataFrame.__getitem__(self, key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3502'>3503</a> if self.columns.nlevels > 1:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3503'>3504</a>     return self._getitem_multilevel(key)
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3504'>3505</a> indexer = self.columns.get_loc(key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3505'>3506</a> if is_integer(indexer):
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3506'>3507</a>     indexer = [indexer]


    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3623, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3622'>3623</a>     raise KeyError(key) from err
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3623'>3624</a> except TypeError:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3624'>3625</a>     # If we have a listlike key, _check_indexing_error will raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3625'>3626</a>     #  InvalidIndexError. Otherwise we fall through and re-raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3626'>3627</a>     #  the TypeError.
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3627'>3628</a>     self._check_indexing_error(key)


    KeyError: 'image'



```python
len(df['image'].unique())
```




    11




```python
df['distortion'].unique()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3621, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3619'>3620</a> try:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:136, in pandas._libs.index.IndexEngine.get_loc()


    File ~/.local/lib/python3.8/site-packages/pandas/_libs/index.pyx:163, in pandas._libs.index.IndexEngine.get_loc()


    File pandas/_libs/hashtable_class_helper.pxi:5198, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    File pandas/_libs/hashtable_class_helper.pxi:5206, in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'distortion'

    
    The above exception was the direct cause of the following exception:


    KeyError                                  Traceback (most recent call last)

    /home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb Cell 36' in <cell line: 1>()
    ----> <a href='vscode-notebook-cell:/home/jan/Documents/VW/Dokumentation_Seminar_IQP.ipynb#ch0000034?line=0'>1</a> df['distortion'].unique()


    File ~/.local/lib/python3.8/site-packages/pandas/core/frame.py:3505, in DataFrame.__getitem__(self, key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3502'>3503</a> if self.columns.nlevels > 1:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3503'>3504</a>     return self._getitem_multilevel(key)
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3504'>3505</a> indexer = self.columns.get_loc(key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3505'>3506</a> if is_integer(indexer):
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/frame.py?line=3506'>3507</a>     indexer = [indexer]


    File ~/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py:3623, in Index.get_loc(self, key, method, tolerance)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3620'>3621</a>     return self._engine.get_loc(casted_key)
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3621'>3622</a> except KeyError as err:
    -> <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3622'>3623</a>     raise KeyError(key) from err
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3623'>3624</a> except TypeError:
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3624'>3625</a>     # If we have a listlike key, _check_indexing_error will raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3625'>3626</a>     #  InvalidIndexError. Otherwise we fall through and re-raise
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3626'>3627</a>     #  the TypeError.
       <a href='file:///home/jan/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py?line=3627'>3628</a>     self._check_indexing_error(key)


    KeyError: 'distortion'



```python
len(df['distortion'].unique())
```




    11



# 1. Stauchung vs. Streckung

Hier wollen wir unsere erste Hypothese mit Hilfe visueller Aufbereitung der Daten untersuchen.

Zuerst stellen wir die relative Häufigkeitsverteilung der Verzerrgrade dar. Dabei gilt eine Response als die Antwort des Subjektes, dass das Bild verzerrt ist.


```python
dfrel = df.groupby(['distortion']).sum() #results in "response" column
dfcopy = df.copy(deep=True) #create deep copy to not overwrite source df
dfcopy.drop(['image','category'],axis=1,inplace=True) #columns "image" and "category" not relevant for this plot
dfrel['total'] = dfcopy.groupby(['distortion']).count() #groupby in order to get values for each distortion rate
dfrel['relative'] = (dfrel['response']/dfrel['total'])*100 #get frequency in percentages
dfrel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>distortion</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>84</td>
      <td>84</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>60</th>
      <td>79</td>
      <td>84</td>
      <td>94.047619</td>
    </tr>
    <tr>
      <th>70</th>
      <td>77</td>
      <td>84</td>
      <td>91.666667</td>
    </tr>
    <tr>
      <th>80</th>
      <td>51</td>
      <td>84</td>
      <td>60.714286</td>
    </tr>
    <tr>
      <th>90</th>
      <td>16</td>
      <td>84</td>
      <td>19.047619</td>
    </tr>
    <tr>
      <th>100</th>
      <td>46</td>
      <td>420</td>
      <td>10.952381</td>
    </tr>
    <tr>
      <th>110</th>
      <td>25</td>
      <td>84</td>
      <td>29.761905</td>
    </tr>
    <tr>
      <th>120</th>
      <td>36</td>
      <td>84</td>
      <td>42.857143</td>
    </tr>
    <tr>
      <th>130</th>
      <td>67</td>
      <td>84</td>
      <td>79.761905</td>
    </tr>
    <tr>
      <th>140</th>
      <td>62</td>
      <td>84</td>
      <td>73.809524</td>
    </tr>
    <tr>
      <th>150</th>
      <td>76</td>
      <td>84</td>
      <td>90.476190</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfrel['relative'].plot.bar()
plt.xlabel('Distortion Rate')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_41_0.png)
    


Danach stellen wir die relative Antworthäufigkeit für beide Verzerrkategorien dar, ohne einelne Verzerrgrade zu unterscheiden.


```python
#absolute Häufigkeiten
dfabstotal = df.copy(deep=True)
#create categories based on distortion rate
dfabstotal['distcategory'] = np.where(dfabstotal['distortion']<100, 'stauchung', 'streckung')
dfabstotal['distcategory'] = np.where(dfabstotal['distortion']==100, 'original', dfabstotal['distcategory'])
dfabstotal.drop(['image','category','distortion'],axis=1,inplace=True) #remove irrelevant columns
dfabstotal.groupby(['distcategory']).sum() #results for "response" column
dfabsbars = dfabstotal.groupby(['distcategory']).sum()
#create second df including total number of entries
dfreltotal = dfabsbars.copy(deep=True)
dfreltotal['total'] = dfabstotal.groupby(['distcategory']).count()
#divide total responses by total number of entries
dfreltotal['relative'] = (dfreltotal['response']/dfreltotal['total'])*100
dfreltotal
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>distcategory</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>original</th>
      <td>46</td>
      <td>420</td>
      <td>10.952381</td>
    </tr>
    <tr>
      <th>stauchung</th>
      <td>307</td>
      <td>420</td>
      <td>73.095238</td>
    </tr>
    <tr>
      <th>streckung</th>
      <td>266</td>
      <td>420</td>
      <td>63.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfreltotal['relative'].plot.bar()
plt.xlabel('Distortion Category')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_44_0.png)
    


# 2. Menschen vs. Tiere

In diesem Abschnitt visualisieren wir Daten zur Überprüfung unserer zweiten Hypothese


```python
dfp=df.copy(deep=True)
dfh=df.copy(deep=True)
dfp=dfp[dfp['category']=='p'] #df for pets
dfh=dfh[dfh['category']=='h'] #df for humans
dfp.drop(['image','category'],axis=1,inplace=True)
dfh.drop(['image','category'],axis=1,inplace=True)
```


```python
#calculate relative response frequency for both human and pet images

#pets
dfpgrp=dfp.groupby(['distortion']).sum()
dfpgrp['total']=dfp.groupby(['distortion']).count()
dfpgrp['relative']=(dfpgrp['response']/dfpgrp['total'])*100

#humans
dfhgrp=dfh.groupby(['distortion']).sum()
dfhgrp['total']=dfh.groupby(['distortion']).count()
dfhgrp['relative']=(dfhgrp['response']/dfhgrp['total'])*100
```

**Haustiere**


```python
dfpgrp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>distortion</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>60</th>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>70</th>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>80</th>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>90</th>
      <td>6</td>
      <td>42</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>100</th>
      <td>30</td>
      <td>210</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>110</th>
      <td>8</td>
      <td>42</td>
      <td>19.047619</td>
    </tr>
    <tr>
      <th>120</th>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>130</th>
      <td>32</td>
      <td>42</td>
      <td>76.190476</td>
    </tr>
    <tr>
      <th>140</th>
      <td>23</td>
      <td>42</td>
      <td>54.761905</td>
    </tr>
    <tr>
      <th>150</th>
      <td>36</td>
      <td>42</td>
      <td>85.714286</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfpgrp['relative'].plot.bar()
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_51_0.png)
    


**Menschen**


```python
dfhgrp
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>distortion</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>60</th>
      <td>41</td>
      <td>42</td>
      <td>97.619048</td>
    </tr>
    <tr>
      <th>70</th>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>80</th>
      <td>34</td>
      <td>42</td>
      <td>80.952381</td>
    </tr>
    <tr>
      <th>90</th>
      <td>10</td>
      <td>42</td>
      <td>23.809524</td>
    </tr>
    <tr>
      <th>100</th>
      <td>16</td>
      <td>210</td>
      <td>7.619048</td>
    </tr>
    <tr>
      <th>110</th>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>120</th>
      <td>19</td>
      <td>42</td>
      <td>45.238095</td>
    </tr>
    <tr>
      <th>130</th>
      <td>35</td>
      <td>42</td>
      <td>83.333333</td>
    </tr>
    <tr>
      <th>140</th>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>150</th>
      <td>40</td>
      <td>42</td>
      <td>95.238095</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfhgrp['relative'].plot.bar()
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_54_0.png)
    


**Vergleich Mensch vs. Tier**

Nachdem wir die Antworten für Menschen und Tiere getrennt dargestellt haben, wollen wir die Antwortverteilungen der beiden Kategorien nebeneinander betrachten.


```python
#Add up all responses (human and pet pictures) for each distortion rate and category
dfpivot = df.copy (deep=True)
dfpivot = dfpivot.groupby(['distortion', 'category']).sum().reset_index() #reset_index is needed to undo the grouping after using sum()
dfpivot2 = df.copy(deep = True)
#Count number of responses (human and pet pictures) for each distortion rate and category
dfpivot2 = dfpivot2.groupby(['distortion', 'category']).count().reset_index()
dfpivot3 = pd.merge(dfpivot, dfpivot2, on=['distortion', 'category'])
dfpivot3.drop(['image'],axis=1,inplace=True)
dfpivot3 = dfpivot3.rename(columns={'response_x': 'response', 'response_y': 'total'})
dfpivot3['relative']=(dfpivot3['response']/dfpivot3['total'])*100
dfpivot3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distortion</th>
      <th>category</th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>h</td>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>p</td>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>h</td>
      <td>41</td>
      <td>42</td>
      <td>97.619048</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>p</td>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>4</th>
      <td>70</td>
      <td>h</td>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>5</th>
      <td>70</td>
      <td>p</td>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>80</td>
      <td>h</td>
      <td>34</td>
      <td>42</td>
      <td>80.952381</td>
    </tr>
    <tr>
      <th>7</th>
      <td>80</td>
      <td>p</td>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>8</th>
      <td>90</td>
      <td>h</td>
      <td>10</td>
      <td>42</td>
      <td>23.809524</td>
    </tr>
    <tr>
      <th>9</th>
      <td>90</td>
      <td>p</td>
      <td>6</td>
      <td>42</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>10</th>
      <td>100</td>
      <td>h</td>
      <td>16</td>
      <td>210</td>
      <td>7.619048</td>
    </tr>
    <tr>
      <th>11</th>
      <td>100</td>
      <td>p</td>
      <td>30</td>
      <td>210</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>12</th>
      <td>110</td>
      <td>h</td>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>13</th>
      <td>110</td>
      <td>p</td>
      <td>8</td>
      <td>42</td>
      <td>19.047619</td>
    </tr>
    <tr>
      <th>14</th>
      <td>120</td>
      <td>h</td>
      <td>19</td>
      <td>42</td>
      <td>45.238095</td>
    </tr>
    <tr>
      <th>15</th>
      <td>120</td>
      <td>p</td>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>16</th>
      <td>130</td>
      <td>h</td>
      <td>35</td>
      <td>42</td>
      <td>83.333333</td>
    </tr>
    <tr>
      <th>17</th>
      <td>130</td>
      <td>p</td>
      <td>32</td>
      <td>42</td>
      <td>76.190476</td>
    </tr>
    <tr>
      <th>18</th>
      <td>140</td>
      <td>h</td>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>19</th>
      <td>140</td>
      <td>p</td>
      <td>23</td>
      <td>42</td>
      <td>54.761905</td>
    </tr>
    <tr>
      <th>20</th>
      <td>150</td>
      <td>h</td>
      <td>40</td>
      <td>42</td>
      <td>95.238095</td>
    </tr>
    <tr>
      <th>21</th>
      <td>150</td>
      <td>p</td>
      <td>36</td>
      <td>42</td>
      <td>85.714286</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfpivot3.pivot("distortion", "category", "relative").plot(kind='bar')
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_58_0.png)
    


Beim Auswerten der Daten fiel auf, dass für Haustiere mit Streckungsgrad von 140% viel seltener eine Verzerrung vermutet wurde, als bei weniger stark gestreckten Haustieren. Um das genauer zu untersuchen schauten wir uns die relativen Häufigkeiten bei den einzelnen Bilder des Verzerrungsgrades 140% genauer an.


```python
df140=df[df['distortion']==140] #retrieve all data for a distortion rate of 140%
df140 = df140.groupby(['image']).sum() #get the number of responses for each image
df140t = df[df['distortion']==140]
df140t = df140t.groupby(['image']).count() #get total number of entries for each image
df140r = pd.merge(df140, df140t, on=['image'])
df140r.drop(['distortion_x', 'distortion_y','category'],axis=1,inplace=True)
df140r = df140r.rename(columns={'response_x': 'response', 'response_y': 'total'})
df140r['relative']=(df140r['response']/df140r['total'])*100 #calculate relative responses for each image
df140r
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>image</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>human7</th>
      <td>20</td>
      <td>21</td>
      <td>95.238095</td>
    </tr>
    <tr>
      <th>human8</th>
      <td>19</td>
      <td>21</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>pet7</th>
      <td>18</td>
      <td>21</td>
      <td>85.714286</td>
    </tr>
    <tr>
      <th>pet8</th>
      <td>5</td>
      <td>21</td>
      <td>23.809524</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
df140r['relative'].plot.bar()
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_61_0.png)
    


Das genauere Hinsehen zeigte, dass ein spezifisches Haustier, "pet8" der Grund für den Ausreißer war. Wir entschieden uns deshalb, die Daten für pet8 bei der Auswertung zu ignorieren.


```python
dfpivotn8 = df[df['image']!='pet8'] #get new dataframe excluding outlier pet8
dfpivotn8 = dfpivotn8.groupby(['distortion', 'category']).sum().reset_index()
dfpivot2n8 = df[df['image']!='pet8']
dfpivot2n8 = dfpivot2n8.groupby(['distortion', 'category']).count().reset_index()
dfpivot3n8 = pd.merge(dfpivotn8, dfpivot2n8, on=['distortion', 'category'])
dfpivot3n8.drop(['image'],axis=1,inplace=True)
dfpivot3n8 = dfpivot3n8.rename(columns={'response_x': 'response', 'response_y': 'total'})
dfpivot3n8['relative']=(dfpivot3n8['response']/dfpivot3n8['total'])*100
dfpivot3n8
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distortion</th>
      <th>category</th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>h</td>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>p</td>
      <td>42</td>
      <td>42</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>h</td>
      <td>41</td>
      <td>42</td>
      <td>97.619048</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>p</td>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>4</th>
      <td>70</td>
      <td>h</td>
      <td>38</td>
      <td>42</td>
      <td>90.476190</td>
    </tr>
    <tr>
      <th>5</th>
      <td>70</td>
      <td>p</td>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>80</td>
      <td>h</td>
      <td>34</td>
      <td>42</td>
      <td>80.952381</td>
    </tr>
    <tr>
      <th>7</th>
      <td>80</td>
      <td>p</td>
      <td>9</td>
      <td>21</td>
      <td>42.857143</td>
    </tr>
    <tr>
      <th>8</th>
      <td>90</td>
      <td>h</td>
      <td>10</td>
      <td>42</td>
      <td>23.809524</td>
    </tr>
    <tr>
      <th>9</th>
      <td>90</td>
      <td>p</td>
      <td>6</td>
      <td>42</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>10</th>
      <td>100</td>
      <td>h</td>
      <td>16</td>
      <td>210</td>
      <td>7.619048</td>
    </tr>
    <tr>
      <th>11</th>
      <td>100</td>
      <td>p</td>
      <td>27</td>
      <td>189</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>12</th>
      <td>110</td>
      <td>h</td>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>13</th>
      <td>110</td>
      <td>p</td>
      <td>8</td>
      <td>42</td>
      <td>19.047619</td>
    </tr>
    <tr>
      <th>14</th>
      <td>120</td>
      <td>h</td>
      <td>19</td>
      <td>42</td>
      <td>45.238095</td>
    </tr>
    <tr>
      <th>15</th>
      <td>120</td>
      <td>p</td>
      <td>17</td>
      <td>42</td>
      <td>40.476190</td>
    </tr>
    <tr>
      <th>16</th>
      <td>130</td>
      <td>h</td>
      <td>35</td>
      <td>42</td>
      <td>83.333333</td>
    </tr>
    <tr>
      <th>17</th>
      <td>130</td>
      <td>p</td>
      <td>32</td>
      <td>42</td>
      <td>76.190476</td>
    </tr>
    <tr>
      <th>18</th>
      <td>140</td>
      <td>h</td>
      <td>39</td>
      <td>42</td>
      <td>92.857143</td>
    </tr>
    <tr>
      <th>19</th>
      <td>140</td>
      <td>p</td>
      <td>18</td>
      <td>21</td>
      <td>85.714286</td>
    </tr>
    <tr>
      <th>20</th>
      <td>150</td>
      <td>h</td>
      <td>40</td>
      <td>42</td>
      <td>95.238095</td>
    </tr>
    <tr>
      <th>21</th>
      <td>150</td>
      <td>p</td>
      <td>36</td>
      <td>42</td>
      <td>85.714286</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfpivot3n8.pivot("distortion", "category", "relative").plot(kind='bar')
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_64_0.png)
    



```python
dfcopy3=df.copy(deep=True)
dfcopy3=dfcopy3[dfcopy3['distortion']!=100] #exclude original pictures
dfcopy3=dfcopy3[dfcopy3['image']!='pet8']
dfcopy3=dfcopy3.groupby(['category']).sum() #add number of responses for each category
dfcopy4=df.copy(deep=True)
dfcopy4=dfcopy4[dfcopy4['distortion']!=100]
dfcopy4=dfcopy4[dfcopy4['image']!='pet8']
dfcopy4.drop(['image', 'distortion'],axis=1,inplace=True)
dfcopy3['total']=dfcopy4.groupby(['category']).count() #count total number of entries for each category
dfcopy3['relative']=(dfcopy3['response']/dfcopy3['total'])*100
dfcopy3 #dataframe includes response data for distorted pictures only
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distortion</th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>h</th>
      <td>42000</td>
      <td>315</td>
      <td>420</td>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>p</th>
      <td>37380</td>
      <td>245</td>
      <td>378</td>
      <td>64.814815</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dfcopy3['relative'].plot.bar()
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_66_0.png)
    



```python
dftotalcat = df.copy(deep=True)
dftotalcat=dftotalcat[dftotalcat['image']!='pet8']
#assign labels depending on the distortion rate
dftotalcat['distcategory'] = np.where(dftotalcat['distortion']<100, 'stauchung', 'streckung')
dftotalcat['distcategory'] = np.where(dftotalcat['distortion']==100, 'original', dftotalcat['distcategory'])
dftotalcat.drop(['image', 'distortion'],axis=1,inplace=True)
dftotalcat2 = dftotalcat.groupby(['distcategory', 'category']).sum().reset_index()
dftotalcatrel = dftotalcat.groupby(['distcategory', 'category']).count().reset_index()
dftotalcat2 = pd.merge(dftotalcat2, dftotalcatrel, on=['distcategory', 'category'])
dftotalcat2 = dftotalcat2.rename(columns={'response_x': 'response', 'response_y': 'total'})
dftotalcat2['relative']=(dftotalcat2['response']/dftotalcat2['total'])*100
dftotalcat2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distcategory</th>
      <th>category</th>
      <th>response</th>
      <th>total</th>
      <th>relative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>original</td>
      <td>h</td>
      <td>16</td>
      <td>210</td>
      <td>7.619048</td>
    </tr>
    <tr>
      <th>1</th>
      <td>original</td>
      <td>p</td>
      <td>27</td>
      <td>189</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stauchung</td>
      <td>h</td>
      <td>165</td>
      <td>210</td>
      <td>78.571429</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stauchung</td>
      <td>p</td>
      <td>134</td>
      <td>189</td>
      <td>70.899471</td>
    </tr>
    <tr>
      <th>4</th>
      <td>streckung</td>
      <td>h</td>
      <td>150</td>
      <td>210</td>
      <td>71.428571</td>
    </tr>
    <tr>
      <th>5</th>
      <td>streckung</td>
      <td>p</td>
      <td>111</td>
      <td>189</td>
      <td>58.730159</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use pyplot for plotting the data and seaborn to remove spines
dftotalcat2.pivot("distcategory", "category", "relative").plot(kind='bar')
plt.xlabel('Distortion')
plt.ylabel('Response Frequency in %')
sns.despine()
```


    
![png](Dokumentation_Seminar_IQP_files/Dokumentation_Seminar_IQP_68_0.png)
    


# Ergebnisse

Nach Betrachtung der Daten können wir feststellen, dass diese unsere beiden Hypothesen bestätigen.

# Manöverkritik

Uns sind 3 Ansätze eingefallen, wie man bei einer erneuten Untersuchung der Fragestellung aussagekräftigere Ergebnisse erhalten könnte.

Einmal könnte man statt der prominenten Gesichter den Versuchssubjekten unbekannte Personen abfotografieren - die Haustiere waren den meisten weniger vertraut als Olaf Scholz oder Barack Obama.

Außerdem könnte jedes Versuchsobjekt mit jedem der von uns ausgewählten Verzerrungsgrade verzerrt werden, um den Vergleich zwischen den einzelnen Verzerrungsstufen aussagekräftiger zu machen und Effekte die sich nur bei einer bestimmten Verzerrung eines Bildes gezeigt haben zu verhindern.

Schlussendlich könnte man bei jeder Durchführung des Versuchs die Bilder zufällig anordnen um eventuelle Zusammenhänge zwischen ähnlichen Bildern zu umgehen.

Insgesamt wäre der Versuch aussagekräftiger, wären mehr Daten gesammelt worden.
