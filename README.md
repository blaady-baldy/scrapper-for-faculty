# EXCTRATING EMAIL IDS FROM AN HTML PAGE

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Maintainers


INTRODUCTION
------------

This project aims to store multiple email ids on a page in a csv file.
While scouting different faculty pages of IITs, I discovered that the email ids stored on these pages is in different formats and cannot be detected by the mail regex we use.
That is why I improved my regex in a way to detect and store email ids in multiple formats such as :

* name AT domain DOT com
* name(AT)domain(DOT)com
* name[AT]domain[DOT]com
* name{AT}domain{DOT}com
* name[AT*]domain[DOT*]com



REQUIREMENTS
------------

This module requires Python 3 to be installed in your system.
The different libraries required in the project are Beautiful Soup and Urllib.


INSTALLATION
------------

Install the Extracting Email Ids module by forking or cloning the project in your 
system



MAINTAINERS
-----------

 * Devansh Singh - blaadybaldy@gmail.com


