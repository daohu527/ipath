# ipath
apollo path and simple map making tool

## Draw path
We can use below cmd draw path from cyber_record
```
cyber_record echo -f example.record.00000 -t /apollo/localization/pose | ipath
```

#### Save path
Since it is time-consuming to read the location information from the record file, we can save it to file add `-s`, which is saved to the local `path.txt ` by default.
```
cyber_record echo -f example.record.00000 -t /apollo/localization/pose | ipath -s
```

## Draw from file
After saving path.txt you can read directly from it and draw the path.
```
ipath -i path.txt
```