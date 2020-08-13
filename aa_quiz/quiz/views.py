from django.shortcuts import render, HttpResponse, redirect
import json
import re
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from leads.models import Lead, LeadManager
from .models import Persona
# import matplotlib.pyplot as plt

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
    # render Welcome slide, flush sessions, reset user score
    request.session.flush()
    request.session['user_score'] = 0
    return render(request, 'quiz/index.html')


def q_intent(request):
    # render Intent form and store 'referer'
    request.session['persona_referer'] = '/quiz/intent'
    return render(request, 'quiz/snippets/intent.html')


def process_intent(request):
    # validate
    errors = {}
    if 'intent' not in request.POST:
        errors['intent'] = "Please choose an option."
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quiz/intent')

    else:
        # capture form results and store in sessions
        request.session['intent'] = request.POST['intent']
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
    # render Artwork Info Request form and store 'referer'
    request.session['contact_referer'] = '/quiz/info_request'
    return render(request, 'quiz/snippets/info_request.html')


def process_info_request(request):
    # validate form data:
    errors = {}
    URL_REGEX = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    # if no url entered:
    if 'art-info-url' not in request.POST:
        if 'art-info-artist' not in request.POST:
            errors['need_info'] = "Please enter a URL or the artist's name and title of the work."

        # if 'art-info-artist' in request.POST:
        #     if len(request.POST['art-info-artist']) < 2:
        #         errors['art-info-artist'] = "Artist's name must be more than 2 characters."
        # if 'art-info-title' in request.POST:
        #     if len(request.POST['art-info-title']) < 1:
        #         errors['art-info-title'] = "Please enter the artwork's title."
    # if url entered:
    if not URL_REGEX.match(request.POST['art-info-url']):
        errors['art-info-url'] = "Please enter a valid url."

    if 'art-info-message' not in request.POST:
        errors['art-info-message'] = "Please submit a question that is at least 10 characters in length."
    if 'art-info-message' in request.POST:
        if len(request.POST['art-info-message']) < 5:
            errors['message_length'] = "Please submit a question that is at least 10 characters in length."

    # pass errors to template
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quiz/info_request')

    else: 
        # capture form results and store in sessions
        request.session['art_info_url'] = request.POST['art-info-url']
        request.session['art_artist'] = request.POST['art-info-artist']
        request.session['art_title'] = request.POST['art-info-title']
        request.session['art_message'] = request.POST['art-info-message']

        # score message length and add points for uploading photos:
        if len(request.POST['art-info-message']) > 20:
            request.session['user_score'] += 20
        else: 
            request.session['user_score'] += 0
        if request.FILES:
            request.session['user_score'] += 20
        # redirect to next form
        return redirect('/quiz/contact')


def q_spec_space(request):
    # render Specific Space form and store 'referer'
    request.session['persona_referer'] = '/quiz/spec_space'
    return render(request, 'quiz/snippets/spec_space.html')


def process_spec_space(request):
    # validate
    print(request.POST)
    errors = {}

    if len(request.POST['specspace-num-works']) < 1:
        errors['num_works'] = "Please let us know how many artworks you are looking for."
    if len(request.POST['specspace-message']) < 1:
        errors['specspace_message'] = "Please tell us a bit about your space, wall dimensions, and any other relevant information."

    # pass errors to template
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quiz/spec_space')
        print(errors)

    else:
        # capture form results and store in sessions
        request.session['specspace-num-works'] = request.POST['specspace-num-works']
        request.session['specspace-message'] = request.POST['specspace-message']

        # score message length:
        if len(request.POST['specspace-message']) > 20:
            request.session['user_score'] += 25
        else: 
            request.session['user_score'] += 0
        # redirect to next form
        return redirect('/quiz/persona')


def q_persona(request):
    # render Persona form and store 'referer'
    request.session['contact_referer'] = '/quiz/persona'
    return render(request, 'quiz/snippets/persona.html')


def process_persona(request):
    # reset persona counters
    lw_count = 0
    he_count = 0
    co_count = 0
    na_count = 0

    # if user makes persona selections
    if 'persona' in request.POST:
        # tally persona results
        choices = request.POST.getlist('persona')
        for choice in choices:
            if choice == 'lw':
                lw_count += 1
            elif choice == 'co':
                co_count += 1
            # elif choice == 'he':
            #     he_count += 1
            else:
                he_count += 1
            # else:
            #     na_count = 1
            print(choices)
    else:
        na_count = 1

    # store counts in session for plotting:
    p_scores = {
        'LW': lw_count,
        'HE': he_count,
        'CO': co_count,
        'NA': na_count,
        }
    request.session['p_scores'] = p_scores
    print(p_scores)

    # Note: persona creation happens at submit instance to prevent quiz quitters from creating personas. 
    return redirect('/quiz/category')


def q_category(request):
    # render Category form and store 'referer'
    request.session['contact_referer'] = '/quiz/category'
    return render(request, 'quiz/snippets/category.html')


def process_category(request):
    # process form data
    # score points for each question answered
    request.session['categories'] = request.POST.getlist('category')
    for category in request.session['categories']:
        request.session['user_score'] += 2
    print(request.session['categories'])
    return redirect('/quiz/subject')


def q_subject(request):
    # render Subject form and store 'referer'
    request.session['contact_referer'] = '/quiz/subject'
    return render(request, 'quiz/snippets/subject.html')


def process_subject(request):
    # process form data
    # score points for each question answered
    request.session['subjects'] = request.POST.getlist('subject')
    for subject in request.session['subjects']:
        request.session['user_score'] += 2
    return redirect('/quiz/style')


def q_style(request):
    # render Style form and store 'referer'
    request.session['contact_referer'] = '/quiz/style'
    return render(request, 'quiz/snippets/style.html')


def process_style(request):
    # increase score (minimally) for each question answered
    request.session['styles'] = request.POST.getlist('style')
    for style in request.session['styles']:
        request.session['user_score'] += 2

    return redirect('/quiz/size')


def q_size(request):
    # render Style form and store 'referer'
    request.session['contact_referer'] = '/quiz/size'
    return render(request, 'quiz/snippets/size.html')


def process_size(request):
    # increase score (minimally) for each question answered
    request.session['sizes'] = request.POST.getlist('size')
    for size in request.session['sizes']:
        request.session['user_score'] += 2

    return redirect('/quiz/contact')


def q_contact(request):
    # render Contact form
    return render(request, 'quiz/snippets/contact.html')


def process_contact(request):
    # validate form data:
    errors = Lead.objects.validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quiz/contact')

    else:
        # grab cumulative intent score:
        intent = request.session['user_score']

        # convert session data into json -- json.dumps()
        results = {}
        for key, value in request.session.items():
            results[key] = value
        brief = json.dumps(results)

        # get Boolean newsletter opt-in
        print(request.POST['newsletter'])

        # get image files, if any:
        if 'img_upload' in request.FILES:
            client_upload = request.FILES['img_upload']
        else:
            client_upload = None

        # create new lead in DB
        new_lead = Lead.objects.create(
            first_name=request.POST['contact-first-name'],
            last_name=request.POST['contact-last-name'],
            email_address=request.POST['contact-email'],
            phone_number=request.POST['contact-phone'],
            budget_min=request.POST['contact-budget-min'],
            budget_max=request.POST['contact-budget-max'],
            uploads=client_upload,
            quiz_brief=brief,
            newsletter_opt_in=request.POST['newsletter'],
            intent_score=intent,
            )
        print(f'Lead created: {new_lead.first_name} {new_lead.last_name}')
    
        # DETERMINE PERSONA OF NEW LEAD
        # find max values to determine earned persona:
        if 'p_scores' in request.session:
            p_scores = request.session['p_scores']
        else:
            p_scores = {
                'LW': 0,
                'HE': 0,
                'CO': 0,
                'NA': 1,
                }
        max_val = max(p_scores.values())
        max_keys = [k for k, v in p_scores.items() if v == max_val]
        print(max_keys, max_val)
            

        # PERSONA TYPES AND IDs:
        # 1 - LIVING WELL
        # 2 - HIP ENTHUSIAST
        # 3 - COLLECTOR
        # 4 - UNKNOWN
        for key in max_keys:
            if key == 'LW':
                this_persona = Persona.objects.get(id=1)
                this_persona.has_leads.add(new_lead)
                print(f'Persona created: {this_persona.persona_type}')
            elif key == 'HE':
                this_persona = Persona.objects.get(id=2)
                this_persona.has_leads.add(new_lead)
                print(f'Persona created: {this_persona.persona_type}')
            elif key == 'CO':
                this_persona = Persona.objects.get(id=3)
                this_persona.has_leads.add(new_lead)
                print(f'Persona created: {this_persona.persona_type}')
            elif key == 'NA':
                this_persona = Persona.objects.get(id=4)
                this_persona.has_leads.add(new_lead)
                print(f'Persona created: {this_persona.persona_type}')

    lead = Lead.objects.get(id=new_lead.id)
    result_id = lead.id

    # redirect to q_results
    return redirect(f'/quiz/result/{result_id}')


def q_result(request, id):
    # render quiz Results page
    context = {
        'this_lead': Lead.objects.get(id=id)
    }
    return render(request, 'quiz/snippets/result.html', context)