# Contact Searching

doThis: Make sure that you delete all of the doThis markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Annaliese Stone

## Program Output

### What is the output from running the following commands?

doThis: Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
File "C:\Users\katni\Desktop\CMPSC\CMPSC102\classDocs\surveys\08_survey_contact_searching-annaliese-stone\contactsearcher\contactsearcher\main.py", line 40, in contactsearcher
    contacts = search.contacts
AttributeError: module 'contactsearcher.search' has no attribute 'contacts'
```

doThis: Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
File "C:\Users\katni\Desktop\CMPSC\CMPSC102\classDocs\surveys\08_survey_contact_searching-annaliese-stone\contactsearcher\contactsearcher\main.py", line 40, in contactsearcher
    contacts = search.contacts
AttributeError: module 'contactsearcher.search' has no attribute 'contacts'
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

doThis: Use a fenced code block to provide the requested source code
```
from contactsearcher import search
```

doThis: Write at least one paragraph to explain the request source code
This line of code imports the `search.py` file from `contactsearcher` folder. This is the same folder that the `main.py` file is located in. It's placed at the vry top of the document, alongsidethe other import functions. 

#### The source code statement that extracts the current job description for a contact

doThis: Use a fenced code block to provide the requested source code
```
#search.py
...
with open(main.contacts_file, newline='') as file:
        file = csv.DictReader(main.contacts_file)
        # doThis: iterate through each line of the file and extract the current job
        # ---> doThis: extract the current job for the contact on this line of the CSV
        for row in file:
            print(row[contacts], row[job_description])
            List[contacts] = [job_description]
```

doThis: Write at least one paragraph to explain the request source code
The file that was specified in the main file is opened, and the CSV Dictionary Reader allows for the file to be read through line by line in a for loop. Each row's contact (email) and job description is printed, and then the two are paired in the List dictionary. 

#### Invocation of the function called `search_for_email_given_job`

doThis: Use a fenced code block to provide the requested source code
```
# doThis: perform the search for all of the relevant email addresses given the job description
    contacts_list = search.search_for_email_given_job(job_description, contacts_text)
```
doThis: Write at least one paragraph to explain the request source code
`search_for_email_given_job` is invoked from the `search.py` file. The arguments `job_description` and `contacts_text` are given. 

#### Test case for the function called `search_for_email_given_job`

doThis: Use a fenced code block to provide the requested source code
```
def test_find_one_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("writer", contacts_database)
    assert len(contacts_list) == 1
```

doThis: Write at least one paragraph to explain the request source code
The test creates a database of contacts, and then calls on the `search_for_email_given_job` function to look for jobs with the name "writer." It then check for their to be only one contact with the job "writer."

#### Execute trace of the `contactsearcher` program

doThis: Explain each function call that takes place for the following run of the program
doThis: Write at least one paragraph to explain every function call when running `contactsearcher`
doThis: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
