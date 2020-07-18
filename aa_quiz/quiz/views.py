from django.shortcuts import render, HttpResponse, redirect
from leads.models import Lead
from .models import Persona
# Create your views here.

''' TEMPLATE FOR MAIN VIEWS: 

def q_view(request):
    # check that form is valid: 
    if not in request.session:
        ...code here...
        return redirect('quiz/view)
    
    context = {
        'url_next' = '',
        'url_back' = '',
    }
    return render(request, 'quiz/view.html)


def process_view(request):
    # capture form results and store in session:
    # if applicable, set conditions to determine where to redirect
    if request.POST == x:
        return redirect('quiz/view_x')
    elif request.POST == y:
        return redirect('quiz/view_y')
    else:
        return redirect('quiz/view_z')
    # or, return redirect('quiz/next_view')

'''


def q_welcome(request):
    # flush previous session
    request.session.flush()
    # set new user score to 0
    request.session['user_score'] = 0
    # Render the welcome slide for AA Quiz
    return render(request, 'quiz/index.html')


def q_intent(request):
    # render Intent form
    return render(request, 'quiz/snippets/intent.html')


def process_intent(request):
    # capture form results and store in sessions
    request.session['intent'] = request.POST['intent']
    print(request.session['intent'])
    # redirect to appropriate form
    if request.POST['intent'] == 'info-request':
        request.session['user_score'] += 30
        return redirect('/quiz/info_request')

    elif request.POST['intent'] == 'spec-space':
        request.session['user_score'] += 20
        return redirect('/quiz/spec_space')
    else:
        request.session['user_score'] += 5
        return redirect('/quiz/persona')


def q_info_request(request):
    # render Artwork Information Request form
    return render(request, 'quiz/snippets/info_request.html')


def process_info_request(request):
    # capture form results and store in sessions
    request.session['art_info_url'] = request.POST['art-info-url']
    request.session['art_artist'] = request.POST['art-info-artist']
    request.session['art_title'] = request.POST['art-info-title']
    request.session['art_message'] = request.POST['art-info-message']

    #score message lenght:
    if len(request.POST['art-info-message']) > 100:
        request.session['user_score'] += 25
    elif len(request.POST['art-info-message']) > 50:
        request.session['user_score'] += 15
    else: 
        request.session['user_score'] += 0

    # redirect to next form
    return redirect('/quiz/contact')


def q_spec_space(request):
    # render Specific Space form
    return render(request, 'quiz/snippets/spec_space.html')


def process_spec_space(request):
    request.session['num_works'] = request.POST['specspace-num-works']
    request.session['specspace_message'] = request.POST['specspace-message']
    
    # will need to handle multiple image upload:
    # request.session['images'] = request.POST['img_upload']

    return redirect('/quiz/persona')


def q_persona(request):
    # render Persona form
    return render(request, 'quiz/snippets/persona.html')


def process_persona(request):
    living_well_count = 0
    hip_enthus_count = 0
    collector_count = 0
    
    # tally persona results
    choices = request.POST.getlist('persona')
    for choice in choices:
        if choice == 'lw':
            living_well_count += 1
        elif choice == 'co':
            collector_count += 1
        elif choice == 'he':
            hip_enthus_count += 1
        else:  # if choice == he-co
            collector_count += 1
            hip_enthus_count += 1
    
    # store persona data in session:
    request.session['living_well'] = living_well_count
    request.session['hip_enthus'] = hip_enthus_count
    request.session['collector'] = collector_count

    print(choices)
    print(living_well_count)
    print(hip_enthus_count)
    print(collector_count)
            
    return redirect('/quiz/category')


def q_category(request):
    # render Category form
    return render(request, 'quiz/snippets/category.html')


def process_category(request):
    # increase score (minimally) for each question answered
    categories = request.POST.getlist('category')
    for category in categories:
        request.session['user_score'] += 2
    return redirect('/quiz/subject')


def q_subject(request):
    # render Subject form
    return render(request, 'quiz/snippets/subject.html')


def process_subject(request):
    # increase score (minimally) for each question answered
    subjects = request.POST.getlist('subject')
    for subject in subjects:
        request.session['user_score'] += 2
    return redirect('/quiz/style')


def q_style(request):
    # render Style form
    return render(request, 'quiz/snippets/style.html')


def process_style(request):
    # increase score (minimally) for each question answered
    styles = request.POST.getlist('style')
    for style in styles:
        request.session['user_score'] += 2
    return redirect('/quiz/contact')


def q_contact(request):
    # render Contact form
    return render(request, 'quiz/snippets/contact.html')


def process_contact(request):
    # calculate persona score and intent score
    persona = Persona.objects.create(persona_type="HIP ENTHUSIAST")
    intent = 10
    # create new lead in DB
    new_lead = Lead.objects.create(
        first_name=request.POST['contact-first-name'],
        last_name=request.POST['contact-last-name'],
        email_address=request.POST['contact-email'],
        phone_number=request.POST['contact-phone'],
        budget_min=request.POST['contact-budget-min'],
        budget_max=request.POST['contact-budget-max'],
        newsletter_opt_out=request.POST['contact-newsletter'],
        intent_score=intent,
        persona_type=persona,
        )
    print(f'Lead created: {new_lead.first_name} {new_lead.last_name}')

    # convert session data into json -- json.dumps()
    # redirect to q_results
    return redirect('/quiz/result')


def q_result(request):
    # render quiz Results page
    return render(request, 'quiz/snippets/result.html')
