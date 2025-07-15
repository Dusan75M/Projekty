# Engeto project no. 3

3rd project of Python Academy by Engeto.

## Description of the project

This project is used to extract results from the 2017 parliamentary elections. You can find the link to view [here](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Libraries installation

Libraries that are used in the code are stored in the file `requirements.txt`. For installation, I recommend using a new virtual environment and with the manager installed, run as follows:

`$ pip3 --version                    # check the manager version
$ pip3 install -r requirements.txt  # install the libraries`

## Project launch

Running main.py from the command line requires two mandatory arguments.

`python main.py <territorial-unit-link> <results-file>`

The results will then be downloaded as a file with the .csv extension.

## Project example

Voting results for the Prostějov district:

`1st argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2nd argument: results_prostejov.csv`

Program launch:

`python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "results_prostejov.csv"`

Download progress:

`DOWNLOADING DATA FROM THE CHOSEN URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
SAVING DATA INTO THE FILE: results_prostejov.csv
ENDING electoral scraper`

Partial output:

`code;location;registered;envelopes;valid;...
506761;Alojzov;205;145;144;29;0;0;9;0;5;17;4;1;1;0;0;18;0;5;32;0;0;6;0;0;1;1;15;0
589268;Bedihošť;834;527;524;51;0;0;28;1;13;123;2;2;14;1;0;34;0;6;140;0;0;26;0;0;0;0;82;1
...`