"""Search for an email address given a fragment of a job description."""

from typing import List
from contactsearcher import main

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # doThis: create an empty list of the contacts
    List = {}
    # doThis: iterate through the file, parsing it line by line
    # doThis: refer to the file called input/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    with open(main.contacts_file, newline='') as file:
        file = csv.DictReader(main.contacts_file)
        # doThis: iterate through each line of the file and extract the current job
        # ---> doThis: extract the current job for the contact on this line of the CSV
        for row in file:
            print(row[contacts], row[job])
            List[contacts] = [job]

    # ---> doThis: the job description matches and thus we should save it in the list
    for contacts, job in List:
        if job == main.job_description:
            # doThis: return the list of the contacts who have a job description that matches
            return True
        else:
            return False
