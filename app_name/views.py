from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import StudentProfileForm, CollegePreferenceForm
from .models import StudentProfile, University, Major, AdmissionScore, CollegePreference
from django.db.models import Q, Avg

@login_required
def home(request):
    """高考志愿填报助手首页"""
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = None
    
    context = {
        'profile': profile,
    }
    return render(request, 'app_name/home.html', context)

@login_required
def student_profile_create(request):
    """创建学生档案"""
    try:
        profile = request.user.studentprofile
        return redirect('profile_detail')
    except StudentProfile.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = StudentProfileForm()
    
    return render(request, 'app_name/profile_form.html', {'form': form})

@login_required
def profile_detail(request):
    """查看学生档案"""
    profile = get_object_or_404(StudentProfile, user=request.user)
    return render(request, 'app_name/profile_detail.html', {'profile': profile})

@login_required
def university_list(request):
    """大学列表"""
    universities = University.objects.all()
    
    province_filter = request.GET.get('province')
    type_filter = request.GET.get('type')
    
    if province_filter:
        universities = universities.filter(province=province_filter)
    if type_filter:
        universities = universities.filter(university_type=type_filter)
    
    context = {
        'universities': universities,
        'province_filter': province_filter,
        'type_filter': type_filter,
    }
    return render(request, 'app_name/university_list.html', context)

@login_required
def university_detail(request, pk):
    """大学详情"""
    university = get_object_or_404(University, pk=pk)
    admission_scores = AdmissionScore.objects.filter(
        university=university,
        subject_type=request.user.studentprofile.subject_type
    ).order_by('-year')[:5]
    
    context = {
        'university': university,
        'admission_scores': admission_scores,
    }
    return render(request, 'app_name/university_detail.html', context)

@login_required
def major_list(request):
    """专业列表"""
    majors = Major.objects.all()
    category_filter = request.GET.get('category')
    
    if category_filter:
        majors = majors.filter(category=category_filter)
    
    context = {
        'majors': majors,
        'category_filter': category_filter,
    }
    return render(request, 'app_name/major_list.html', context)

@login_required
def major_detail(request, pk):
    """专业详情"""
    major = get_object_or_404(Major, pk=pk)
    context = {
        'major': major,
    }
    return render(request, 'app_name/major_detail.html', context)

@login_required
def recommendation(request):
    """志愿推荐"""
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        return redirect('profile_create')
    
    # 根据分数推荐大学
    recommended_universities = University.objects.filter(
        admission_scores__province=profile.province,
        admission_scores__subject_type=profile.subject_type,
        admission_scores__min_score__lte=profile.total_score
    ).distinct().order_by('-ranking')[:10]
    
    # 查看已填报的志愿
    preferences = CollegePreference.objects.filter(
        student=profile
    ).order_by('preference_order')
    
    context = {
        'profile': profile,
        'recommended_universities': recommended_universities,
        'preferences': preferences,
    }
    return render(request, 'app_name/recommendation.html', context)

@login_required
def preference_create(request):
    """添加志愿"""
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        return redirect('profile_create')
    
    if request.method == 'POST':
        form = CollegePreferenceForm(request.POST)
        if form.is_valid():
            preference = form.save(commit=False)
            preference.student = profile
            preference.save()
            return redirect('recommendation')
    else:
        form = CollegePreferenceForm()
    
    return render(request, 'app_name/preference_form.html', {'form': form})

@login_required
def preference_delete(request, pk):
    """删除志愿"""
    preference = get_object_or_404(CollegePreference, pk=pk, student__user=request.user)
    preference.delete()
    return redirect('recommendation')
