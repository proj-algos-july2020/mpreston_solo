from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def q_welcome(request):
    # Render the welcome slide for AA Quiz
    request.session
    return render(request, 'quiz/index.html')


def q_intent(request):
    # render Intent form
    # context = {
    #     'url_next': '/quiz/contact',
    #     'url_back': '/quiz/welcome',
    # }
    return render(request, 'quiz/snippets/intent.html')


def process_intent(request):
    # capture form results and store in sessions
    request.session['intent'] = request.POST['intent']
    print(request.session['intent'])
    # redirect to appropriate form
    if request.POST['intent'] == 'info-request':
        return redirect('/quiz/contact')
    elif request.POST['intent'] == 'spec-space':
        return redirect('/quiz/info_request')
    else:
        return redirect('/quiz')


def q_info_request(request):
    # render Artwork Information Request form
    return render(request, 'quiz/snippets/info_request.html')


def process_info_request(request):
    # capture form results and store in sessions
    request.session['art_url'] = request.POST['art-info-url']
    request.session['art_artist'] = request.POST['art-info-artist']
    request.session['art_title'] = request.POST['art-info-title']
    request.session['art_message'] = request.POST['art-info-message']
    for item in request.session.items():
        print(item)
    # redirect to next form
    # conditionals
    return redirect('/quiz')
 

def q_spec_space(request):
    # render Specific Space form
    pass


def q_persona(request):
    # render Persona form
    pass


def q_category(request):
    #render Category form
    pass


def q_subject(request):
    # render Subject form
    pass


def q_style(request):
    # render Style form
    pass


def q_contact(request):
    # render Contact form
    return render(request, 'quiz/snippets/contact.html')


def process_contact(request):
    # capture form results and store in session
    
    # create new lead in DB

    # redirect to q_results
    return HttpResponse("sending you to the results page")


def q_result(request):
    # render quiz Results page
    pass

