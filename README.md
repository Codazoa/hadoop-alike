# Hadoop-alike cs454

Name: Cody Vernon

This project mimics the streaming capabilities of hadoop. The provided files **mapper.py** and **reducer.py** are made to work for the specific data in **input.dat**.

I tried multiple methods for getting hadoop working on my system and all failed. I had to resort to the shortcut to emulate streaming. These are instructions for linux.

### To run
`cat input.dat | ./mapper.py | sort | ./reducer.py >> outputfile`

If this does not work, the permissions for **mapper.py** and **reducer.py** may be messed up. Be sure both files have execute permission.
`sudo chmod u+x mapper.py reducer.py`

### Output
```
$20{visits} 2
$20{size} 13682
0055_6715_45_auto_collectors{visits} 3
0055_6715_45_auto_collectors{size} 3114
007:_Nightfire{visits} 12
007:_Nightfire{size} 100074
00{visits} 8
00{size} 54668
...
...
...
```
