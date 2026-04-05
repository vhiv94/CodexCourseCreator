# let's reassess this project 

- @.cursor/rules/ 
- @course/ 
- @scripts/ 

### I don't really like the output 

- @python/reference-module/Ch1/L1.md. 
- @python/fundamentals/Ch1/L1.md 
- @python/data-structures/Ch1/L1.md 
- @python/backend-fundamentals-kanban/Ch1/L1.md 

### a couple complaints: 

1. the lessons are far too broad. they should be more specific.
2. I don't really care if rules have a name or personality
3. it feels like the spine is too rigid. the process should be a bit more dynamic if needed 

### project scope/flow

1. decide the subject matter
    1. if the request is too broad, try to narrow it down with questions
    2. if the request is too narrow, try to expand it with questions
    3. perform a surface level knowledge assessment to determine what concepts need a deep dive or just a review
2. break that subject matter into modules, chapters, and lessons 
    1. course length:
        - a particularly long module might contain 10+ chapters, and on average something like 6 chapters 
        - a particularly long chapter might contain 15+ lessons, and on average something like 8 lessons
        - if the planned course can be summed up in 1 or 2 modules, then it should not use the module structure
        - a course can contain as many modules as necessary
    2. modules:
        - basically a course within a course
        - modules should encompass a broad concept, like fundamentals or OOP
        - they are needed because we want to have long and short courses
        - examples:
            - in a fundamentals course modules might not be necessary
            - in a back-end fundamentals: 
                - the database 
                - requests
                - the server 
                - dataflow 
                - etc.
            - in a "learn a new language": 
                - fundamentals
                - classes/objects (if they're used in that language)
                - Networks (internet)
                - etc.
    3. chapters:
        - each chapter should encapsulate a more narrow concept
        - in other words a "leaf" concept
        - examples:
            - in a fundamentals course/module:
                - variables
                - functions
                - basic data structures: (might have their own chapters)
                    - arrays (lists in python)
                    - sets
                    - maps (dictionaries in python)
                - etc.
            - in a requests module of a back-end fundamentals course:
                - response codes
                - GET
                - POST
                - etc.
            - in a classes/objects module "learn a new language" course:
                - class layout: constructor, properties, methods
                - objects and instantiation
                - inheritance
                - etc.
    4. lessons:
        - each lesson should encapsulate a single step of execution
        - build upon each other to explain implementation
        - some lessons can be quizes to review freshly learned information, but use them sparingly
        - examples:
            - in a variables chapter:
                - basic types: int, float, str
                - declaration
                - assignment
                - etc.
            - in a response codes chapter: (probably a shorter chapter)
                - level: success (200), server(300), error (400)
                - common codes:
                    - 200
                    - 404
                    - 307
                - etc.
            - in an objects and instantiation chapter:
                - what is an object?
                - instantiat an object
                - pass an object to a function
                - create an object inside a function call
                - etc.
    5. knowledge assessments:
        - an initial test in the course creation step to gauge the students current knowledge
            - this assessment should be very surface level
            - we just want to get a scope of the course
        - quizes in some lessons and at the end of chapters for review and to help with knowledge retention
        - maybe random pop quizes on previous lessons before generating a chapter (if we decide not to generate the whole course up front)
    6. students knowledge level:
        - the knowledge level of the student should provide scope to the course
        - just because the student is knowledgeable in a subject, don't assume they know everything
        - the course should be dynamic and adapt to the student as they learn 
        - nothing should be skipped because the student knows it. 
            - review is very valuable in learning as it gives unfamiliar/new knowledge a place to go
3. should we generate the whole course up front or chapter by chapter?
    1. short answer: I don't know yet
    2. it might be best to decide this in the course scoping step
        - if it's a fundamentals course, perhaps we have a template that gets adjusted subtly to the student's knowledge assessment
        - if we want to go chapter by chapter there could be deeper (not too deep) assessments of the next concept
        - or maybe we assess what concept to explore next, such that the course is more dynamic
            - in this case there wouldn't be a "spine" yaml like we currently have or it might be very basic
4. generation step:
    - I've explored these possibilities already in this document so just to review:
    - we could have quizes before and at the end of chapters (whether or not we go chapter by chapter)
    - I don't think lesson by lesson would be prudent for the *final product* (a website version of this course creator)
        - basically it would be too expensive
        - maybe this means generating more content at a time is prefered
        - so chapter generation would include each lesson, the quiz/test at the end, **and** the assessment to determine the next chapter/concept (or it's content if the spine is detailed enough)

### how can we improve this process? 

- I like having a coherent project in stead of isolated "toy code"
    - though the project could be reused for future courses
    - or on the flip side a course could have more than one project
    - the project itself can be a "toy project". 
    - the point is more about progression 
    - and keeping the interest of the student (a reason to continue/come back)
- the names and personality might be nice for a final project, but is unnecesary for now
    - let's remove this convention in the rules
    - eventually I want to make this a website, but we are far from that right now
- are rules even the way to go?
    - let's definitely make an AGENTS.md to explain the scope/flow explained above
    - if we use rules the agents file can help determine which one is used based on the prompt
    - I want to make it more automatic for now
- we might want to have a separate SCOPE file and FINAL_PRODUCT file, to keep context/AGENTS file clean
    - the scope is explained above, we have it explained in detail in the SCOPE file and a short and simple version in AGENTS
    - the FINAL_PRODUCT should be more or less the same, but in the context of a website
        - what differentiates this website is that the courses will be unique to each user
            - we might have templates or other reusable structures on the backend for course creation
            - we might have a community forum where students can get help from other students
        - the website will have the following features:
            - a course creator: basically the student provides a single prompt, then answers the necessary questions to define the scope of the course
            - a course list: specific to each user because these will be personalized
            - maybe a course manager: some way of changing a course or regenerating it 
            - and of *course* the course viewer:
                - should pick up where you left off
                - dual pane view lesson on the left, rudimentary text editor on the right
                - a nav: chapter dropdown, lesson dropdown, prev lesson button `<-`, next lesson button `->`
- btw, do these files ***have*** to go  in the root or can we put them in @.cursor/?
    - if I transition away from using cursor I will need to change how the rules are stored anyway
    - if so let's move CHATLOG there too
    - ROADMAP can stay in root as it pertains to the project
