# Chapter 1 Prechapter Assessment

This prechapter assessment happens before the numbered Chapter 1 lesson batch. It is not a replacement for `Ch1/L1` through `Ch1/L4`; it is a short routing step that helps decide how much review, pacing, and explanation the learner will need inside those lessons.

Short bullet answers are fine. Uncertainty is useful information here.

## How to answer

- Answer in your own words instead of trying to sound formal.
- If you feel unsure, say what you think and what still feels fuzzy.
- Use examples from APIs or web apps you have used if that helps you reason.

## Prompts

1. **Server and process mental model**
   What is the difference between a script that runs once and exits versus a server process?

   A script that runs once then exits can take in data, mutate it, and spit it back out, like a simple cli. It can also define a run loop like games do, however it will eventually hit an end condition where the script exits and returns to the operating system. The operating system can also call to exit the script, i.e. clicking the 'x' in a window created by the script.

   a server process will want to be continuously running, it will not want to be exited by the operating system (and I think ideally the machine it's run on would be a linux machine which would be less of an operating system, simply a kernal. I don't deeply understand these implications, yet). the server process wouldn't want to be interrupted by an error as well, so handling of errors will be paramount.

   What does it mean for a backend to "listen" for requests?

   the server should always be waiting for a message to be sent to it's IP address for processing. 

2. **HTTP request and response basics**
   If a client sends `GET /health`, what information is the request asking for?

   I guess whether or not the server process is still running? or in more complex setups, if machines down the chain are still running.

   What should a useful response communicate back?

   I guess the server is running and awaiting a request, or is not running and the client should recontact DNS for a second IP address?

   Why is JSON a reasonable default response format for this course?

   I have no idea, I guess it's somewhat universal?

3. **Routes and resources**
   What resource does `/boards` represent?

   I guess a database, or perhaps a section of a database

   Why might `/boards/{board_id}/columns` be a better early-course route than a flat `/columns` endpoint with no board context?

   no clue.

4. **Status and error expectations**
   When would you expect each of these statuses: `200`, `201`, `404`, `405`, `400`, `422`?

   the only ones I know off the top off my head are 200 (success) and 404 (page not found), I think both of these still get an html page sent to the client, but the  404 one is a specific page denoting that the url you requested is not available. 200 would send the client a page corresponding to the url requested.

   What makes an error payload helpful to a client instead of frustrating?

   no clue.

5. **Capstone reasoning**
   Imagine the frontend tries to create a task in a column that belongs to a different board than the one in the URL. How should the backend respond, and why?

   error, because the request could be malicious? 

6. **Light SQL vocabulary check**
   What do you think SQLite is doing for this project?

   providing the database management api or the database itself in addition to that, I don't know exactly

   In plain language, what is the difference between a table and a row?

   a table contains rows, I know that for sure. the table gets its structure from columns which house the data, and each row contains an entry for each column.
   the column can be  optional, but will be expecting a specific data type to decide how to store and interperate it.

7. **Light deployment vocabulary check**
   What do the terms `domain`, `health check`, and `reverse proxy` currently mean to you?

   domain is the name of the website (before the `.com`), a health check is a specific request to get the status of the server, and all I know about reverse proxy is  that it's a way to host locally and still get routed from dns.

   Which of those feels most familiar, and which feels most uncertain?

   sql/the database, though I still need a review
   
## Routing notes

- Strong Chapter 1 readiness means the learner can mostly explain the health-check contract, the shape of a create/list API, nested resource ownership, and the difference between common status/error categories.
- Review-heavy Chapter 1 pacing is still appropriate if the learner mixes up methods, paths, bodies, resource boundaries, or the difference between not found versus invalid input versus wrong method.
- The outcome of this prechapter assessment should tune pacing and emphasis only. It should not renumber the existing `Ch1/L1` through `Ch1/L4` lesson or test contract.
