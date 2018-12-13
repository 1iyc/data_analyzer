# data_analyzer
Data Analyze before Train

## data_preprocess.py
Delete Which Words or Characters

### Default Function
1. Replace Lower Case to Upper Case
2. Replace "." to ''(None)
3. Replace Specific Character(except "-") to " "(White Space)
4. Delete "-" at Both Ends of Words

### DN or DS
DN: Replace Dash to None (With Default Function Phase 2.)
```commandline
python data_preprocess.py --DN=True
```
DS: Replace Dash to Space (With Default Function Phase 3.)
```commandline
python data_preprocess.py --DS=True
```

### SC
Delete Single Character\
Be Processed After Default Function Phase 4.
```commandline
python data_preprocess.py --SC=True
```

### DC
Delete Word with Duplicated Character (cf. XX, MMM)\
Be Processed After Default Function Phase 4.\
With SC Option, Processing with SC
```commandline
python data_preprocess.py --DC=True
```

### NA
Delete NA Word in NA File Path\
Be Processed at the Last
```commandline
python data_preprocess.py --NA=[NA List File Path]
```

### Other
Combination of Possible Options
```commandline
--DN=True --SC --DC --NA
--DS --SC --DC --NA
--DN --SC --DC
--DN --SC --NA
--DN --DC --NA
--DS --SC --DC
--DS --SC --NA
--DS --DC --NA
--SC --DC --NA
--DN --SC
--DN --DC
--DN --NA
--DS --SC
--DS --DC
--DS --NA
--SC --DC
--SC --NA
--DC --NA
--DN
--DS
--SC
--DC
--NA
None
```

## extract_eval_data.py