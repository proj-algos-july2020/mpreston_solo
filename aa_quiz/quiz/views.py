from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def q_welcome(request):
    # Render the welcome slide for AA Quiz
    request.session
    return render(request, 'quiz/index.html')


def q_intent(request):
    # render Intent form
    return render(request, 'quiz/snippets/intent.html')


def process_intent(request):
    # capture form results and store in sessions, render next form
    request.session['intent'] = request.POST['intent']
    print(request.session['intent'])
    return redirect('/quiz/info_request')


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
    pass


def q_result(request):
    # render quiz Results page
    pass

