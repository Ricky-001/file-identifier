# file-identifier
A simple CLI Tool scripted in Python to check for File types based on MIME types and then comparing them with the extensions.

* Checks the File signature (Magic bytes) for known file MIME types 
* Known signatures are stored in the signatures.py file (can be populated manually to extend known type signatures)
* signatures.py format {'extension' : ['list','of','signatures','in','hex','format']}
* Example extry => {'gif' : ['47 49 46 38 37 61','47 49 46 38 39 61']}
* After checking MIME type, the script also compares the identified type against the file extension (if present)

Based on all the above info, a compiled result is provided

_____

## Usage
<strong>file-id.py</strong> -f FILENAME_TO_SEARCH.EXTENSION <br>
(or simply run the script without arguments and follow the on-screen instructions)
