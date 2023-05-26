from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from ..models import Question

@login_required(login_url='common:login')
def vote_question(request, question_id):
    '''
    질문 추천 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author: #작성자와 추천자가 같으면
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)