# STCD
The Sustainable Transport Communication Dataset

The tools are pure python scripts which make it straightforward to consistently add new resources to the dataset with appropriate metadata. Metadata is hugely important to support construction of large datasets taht are generally usable and reusable.

## Data
Data are located in the "dataset" folder


## Tools
Tools are located in the "tools" folder

## Usage
Duplicate the defaults.cfg file then into a new file, e.g. simon.cfg, then open and edit your new file, adding in your name and email address. This enables analyst name and email to be automatically captured when a new resource is created.

You can now use your new personal config as follows:

```
$ python resources.py http://www.example.com simon.cfg
```


## ToDo

* Tool to validate well-formedness of data - For example, to automatically test pull-requests for complete meta-data before performing a manual inspection.
* Make it so that user supplied configs are read from the etc/config/folder

## Citations

If you use the STCD and wish to cite or otherwise make reference to it then please cite the following:

```
S. Wells & K. Pangbourne (2016) "Using Argumentation Within Sustainable Transport Communication"
Argumentation and Reasoned Action, Proceedings of the 1st European Conference on Argumentation, Lisbon 2015, volume 1, Studies in Logic and Argumentation 62, chapter 34, pp. 781-801, College Publications.
```
or use the following bibtex fragment:

```
@incollection{wells_2016_eca+transport,
    author = {Wells, S. and Pangbourne, K.},
    booktitle = {Argumentation and Reasoned Action, Proceedings of the 1st European Conference on Argumentation, Lisbon 2015, volume 1},
    title = {Using Argumentation Within Sustainable Transport Communication},
    series = {Studies in Logic and Argumentation 62},
    chapter = {34},
    year = {2016},
    pages = {781-801},
    publisher = {College Publications}
    }
```

