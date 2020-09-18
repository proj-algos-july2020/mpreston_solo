
<h2>The Art Advisory Quiz</h2>
<h6>A lead-generation tool for an online art gallery, with customer persona identification logic and 'likelihood-to-convert' scoring.</h6>

<h4>Requirements</h4>

This project was built with <b> Python | Javascript | HTML | CSS | Django | Plotly | JQuery | AJAX | Bootstrap | SQLite </b>
To give it a go, clone this repo, `cd` to the directory where requirements.txt is located, activate your virtualenv, and then install the dependencies listed in `requirements.txt`:    

    pip install -r requirements.txt
    

If you find a problem, feel free to [start an issue](https://github.com/proj-algos-july2020/mpreston_solo/issues).



<h4>Background:</h4>
<p>I work at an online art gallery as an art advisor, and one of our lead-generation 
    tools is an art advisory questionnaire where users can request personalized a selection of 
    personalized artwork suggestions put together by an art advisor. As an art advisor, its my 
    responsibility to respond to these requests by hand-curating a selection of artworks that I 
    think the user will like, based on the information they submitted in their quiz.
</p>
<h4>Problem:</h4> 
<p>The information communicated in the quiz brief is limited to the types of art a lead is interested 
    in reviewing. It does not provide the art advisor with any information about the lead in terms of 
    their likelihood to convert, nor does it identify a lead by what customer persona bucket they fall 
    into. As the business scales and our lead numbers grow, advisors don't know how to prioritize new 
    leads, and a high intent request might wait 5+ days for a response, getting cold (and frustrated!!!).
</p>
<h4>Proposal:</h4>
<p>This project addresses the above issues by creating a new quiz flow that will capture 
    both intent and customer persona type of the user based on their responses. This data will
    (1) help advisors to address high intent leads first, (2) guide users to content that is 
    relevant to them while they wait, and (3) weed out low intent leads. 
</p>
<h4>Product Notes:</h4>
<p>Rather than building a user-facing quiz that reflects what a user might see if they were to take the quiz, 
    I've built an admin-transparent quiz that demonstrates:
    <ol>
        <li>data collection and scoring as users answer quiz questions;</li>
        <li>an end result categorization, based on analysis of the users responses;</li>
        <li>suggestions for relevant content to be served to the user, based on their identified persona type.</li>
    </ol>
</p>
<p>
    When you take the quiz, you will notice a score being awarded as you answer questions. Keep in mind that these scores:
    <ol>
        <li>have arbitrary values, but are meant to show that certain types of inquiries should receive higher value than others;</li>
        <li>would benefit from recalibration after an analysis of users' predicted intent versus actual purchase behaviours;</li>
        <li>do not have an upper limit, but a cap could be determined after some user testing.</li>
    </ol>
</p>

