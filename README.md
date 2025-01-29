# MBTI

[![LGTM](https://lgtm.lol/p/394)](https://lgtm.lol/i/394)

### USE
```bash
# mbti-check_country-ratio
Usage: mbti-check-country-ratio [OPTIONS] MBTI
Try 'mbti-check-country-ratio --help' for help.
╭─ Error ──────────────────────────────────────────────────────────────────────────────────────────────╮
│ Missing argument 'MBTI'.                                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯

$ mbti-check-country-ratio --help

 Usage: mbti-check-country-ratio [OPTIONS] MBTI

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────╮
│ *    mbti      TEXT  [default: None] [required]                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────╮
│ --asc     --no-asc             [default: no-asc]                                                     │
│ --rcnt                INTEGER  [default: 10]                                                         │
│ --help                         Show this message and exit.                                           │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯

$ mbti-check-country-ratio ISFP
         Country  ISFP
       Singapore 10.41
          Brunei 10.41
        Malaysia  9.23
   Faroe Islands  8.99
           China  8.41
         Vanuatu  7.53
         Myanmar  7.53
     Philippines  7.24
         Vietnam  7.18
Papua New Guinea  7.04

$ mbti-check-country-ratio ISFP --asc -rcnt 5
   Country  ISFP
   Lebanon  2.66
   Armenia  2.68
    Serbia  2.71
Montenegro  2.75
   Georgia  2.75

$ mbti-check-type
Usage: mbti-check-type [OPTIONS] MBTI
Try 'mbti-check-type --help' for help.
╭─ Error ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Missing argument 'MBTI'.                                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯

$ mbti-check-type --help

 Usage: mbti-check-type [OPTIONS] MBTI

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    mbti      TEXT  [default: None] [required]                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯

#### check_country_mbti_ratio(mbti: str, asc: bool=False, rcnt: int=10)
```bash
$ pip install DataFollowers-MBTI
$ python
>>> from mbti import check_country_mbti_ratio
>>> check_country_mbti_ratio("ISFP")
            Country   ISFP
0         Singapore  10.41
1            Brunei  10.41
2          Malaysia   9.23
3     Faroe Islands   8.99
4             China   8.41
5           Vanuatu   7.53
6           Myanmar   7.53
7       Philippines   7.24
8           Vietnam   7.18
9  Papua New Guinea   7.04
``` 

### DEV
```bash
$ source .venv/bin/activate
$ pdm add jupyterlab
$ pdm add -dG test pytest

$ git add .
$ git commit -a
$ git push

View at:
https://pypi.org/project/DataFollowers-MBTI/
```

### EDA
- run jupyterlab
```bash
$ jupyter lab
```

### TEST
```bash
$ pytest
$ pytest -s
$ pytest --cov
```

### REF

- [DataSet](https://www.kaggle.com/datasets/yamaerenay/mbtitypes-full/data)
