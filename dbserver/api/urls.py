from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path("helloApi/", views.hello, name='hello'),
    path("helloApi", views.hello, name='hello'),

    # path("get_token/", views.get_token, name='get_token'),

    path("activitynum/", views.activitynum, name='activitynum'),
    path("activitynum", views.activitynum, name='activitynum'),

    path("competitionnum/", views.competitionnum, name='competitionnum'),
    path("competitionnum", views.competitionnum, name='competitionnum'),

    path("examnum/", views.examnum, name='examnum'),
    path("examnum", views.examnum, name='examnum'),

    path("gpa/<int:pk>", views.gpa, name='gpa'),
    path("gpa/<int:pk>/", views.gpa, name='gpa'),

    path("todaycourse/<int:pk>/", views.todaycourse, name='todaycourse'),
    path("todaycourse/<int:pk>", views.todaycourse, name='todaycourse'),


    path("getactivitylist/", views.get_activity_list, name='get_activity_list'),
    path("getactivitylist", views.get_activity_list, name='get_activity_list'),


    # 课程相关
    path("getcourselist/<int:pk>/", views.student_course_list,
         name='student_course_list'),
    path("getcourselist/<int:pk>", views.student_course_list,
         name='student_course_list'),

    path("gettestlist/<int:pk>", views.gettestlist, name='gettestlist'),
    path("gettestlist/<int:pk>/", views.gettestlist, name='gettestlist'),

    path("gett_courselist/<int:pk>/", views.teacher_course_list,
         name='teacher_course_list'),
    path("gett_courselist/<int:pk>", views.teacher_course_list,
         name='teacher_course_list'),

    path("getstudentlist/", views.getstudentlist, name='getstudentlist'),
    path("getstudentlist", views.getstudentlist, name='getstudentlist'),

    path("studentinfo", views.studentinfo, name='studentinfo'),
    path("studentinfo/", views.studentinfo, name='studentinfo'),

    path("teacherinfo/", views.teacherinfo, name='teacherinfo'),
    path("teacherinfo", views.teacherinfo, name='teacherinfo'),

    # 用户信息相关
    path("getStudent/<int:pk>/", views.getStudent, name='getStudent'),
    path("getStudent/<int:pk>", views.getStudent, name='getStudent'),

    path("getTeacher/<int:pk>/", views.getTeacher, name='getTeacher'),
    path("getTeacher/<int:pk>", views.getTeacher, name='getTeacher'),

    path("getaward/<int:pk>/", views.getAward, name='getAward'),
    path("getaward/<int:pk>", views.getAward, name='getAward'),

    path("department/<int:pk>/", views.getDepart, name='getDepart'),
    path("department/<int:pk>", views.getDepart, name='getDepart'),

    path("getExam/<int:pk>/", views.getExam, name='getDepart'),
    path("getExam/<int:pk>", views.getExam, name='getDepart'),

    path("getActivity", views.getActivity, name='getActivity'),
    path("getActivity", views.getActivity, name='getActivity'),

    path("getCompetition", views.getCompetition, name='getCompetition'),
    path("getCompetition/", views.getCompetition, name='getCompetition'),


    path("login/", views.login, name='login'),  # 登入
    path("login", views.login, name='login'),  # 登入

    path("userinfo/<int:pk>", views.userinfo, name='userinfo'),  # 获取用户信息
    path("userinfo/<int:pk>/", views.userinfo, name='userinfo'),  # 获取用户信息


    path("postcom/", views.postcom, name='postcom'),
    path("postcom", views.postcom, name='postcom'),
    path("postact/", views.postact, name='postact'),
    path("postact", views.postact, name='postact'),
    path("postexam/", views.postexam, name='postexam'),
    path("postexam", views.postexam, name='postexam'),

    # 课程相关
    path("getselectedcourse/", views.getselectedcourse, name='getselectedcourse'),
    path("getselectedcourse", views.getselectedcourse, name='getselectedcourse'),
    path("deletecourse/", views.deletecourse, name='deletecourse'),
    path("deletecourse", views.deletecourse, name='deletecourse'),
    path("choosenewcourse/", views.choosenewcourse, name='choosenewcourse'),
    path("choosenewcourse", views.choosenewcourse, name='choosenewcourse'),

    path("startnewcourse", views.startnewcourse, name='startnewcourse'),
    path("startnewcourse/", views.startnewcourse, name='startnewcourse'),

    path("enrollgrade/", views.enrollgrade, name='enrollgrade'),
    path("enrollgrade", views.enrollgrade, name='enrollgrade'),

    path("getgradeanalyse", views.getgradeanalyse, name='getgradeanalyse'),
    path("getgradeanalyse/", views.getgradeanalyse, name='getgradeanalyse'),

    path("joinact/", views.joinact, name='joinact'),
    path("joinact", views.joinact, name='joinact'),

    path("joincom", views.joincom, name='joincom'),
    path("joincom/", views.joincom, name='joincom'),

    path("retakecourse/", views.retakecourse, name='retakecourse'),
    path("retakecourse", views.retakecourse, name='retakecourse'),

    path("getcoursegrade/<int:pk>/", views.getcoursegrade,
         name='getcoursegrade'),
    path("getcoursegrade/<int:pk>", views.getcoursegrade,
         name='getcoursegrade'),

    # 管理员相关
    path("getselectedstudent/", views.getselectedstudent,
         name='getselectedstudent'),
    path("getselectedstudent", views.getselectedstudent, name='getselectedstudent'),

    path("getselectedteacher/", views.getselectedteacher,
         name='getselectedteacher'),
    path("getselectedteacher", views.getselectedteacher, name='getselectedteacher'),

    path("changestudentinfo/", views.changestudentinfo, name='changestudentinfo'),
    path("changestudentinfo", views.changestudentinfo, name='changestudentinfo'),

    path("changeteacherinfo/", views.changeteacherinfo, name='changeteacherinfo'),
    path("changeteacherinfo", views.changeteacherinfo, name='changeteacherinfo'),
    path("changerpinfo/", views.changerpinfo, name='changerpinfo'),
    path("changerpinfo", views.changerpinfo, name='changerpinfo'),

    path("changeclassinfo", views.changeclassinfo, name='changeclassinfo'),
    path("changeclassinfo/", views.changeclassinfo, name='changeclassinfo'),

    path("changedepartmentinfo", views.changedepartmentinfo,
         name='changedepartmentinfo'),
    path("changedepartmentinfo/", views.changedepartmentinfo,
         name='changedepartmentinfo'),

    path("getalldepartment", views.getalldepartment, name='getalldepartment'),
    path("getalldepartment/", views.getalldepartment, name='getalldepartment'),

    path("getallclass/<int:pk>", views.getallclass, name='getallclass'),
    path("getallclass/<int:pk>/", views.getallclass, name='getallclass'),

    path("deletecom/<int:pk>", views.deletecom, name='deletecom'),
    path("deletecom/<int:pk>/", views.deletecom, name='deletecom'),

    path("deleteteacher/<int:pk>/", views.deleteteacher, name='deleteteacher'),
    path("deleteteacher/<int:pk>", views.deleteteacher, name='deleteteacher'),

    path("deletestudent/<int:pk>", views.deletestudent, name='deletestudent'),
    path("deletestudent/<int:pk>/", views.deletestudent, name='deletestudent'),

    path("deleteact/<int:pk>/", views.deleteact, name='deleteact'),
    path("deleteact/<int:pk>", views.deleteact, name='deleteact'),

    path("enrollnewstudent", views.enrollnewstudent, name='enrollnewstudent'),
    path("enrollnewstudent/", views.enrollnewstudent, name='enrollnewstudent'),

    path("enrollnewteacher/", views.enrollnewteacher, name='enrollnewteacher'),
    path("enrollnewteacher", views.enrollnewteacher, name='enrollnewteacher'),

    path("enrollnewdepartment", views.enrollnewdepartment,
         name='enrollnewdepartment'),
    path("enrollnewdepartment/", views.enrollnewdepartment,
         name='enrollnewdepartment'),

    path("enrollnewclass/", views.enrollnewclass, name='enrollnewclasst'),
    path("enrollnewclass", views.enrollnewclass, name='enrollnewclasst'),

    path("enrolltest", views.enrolltest, name='enrolltest'),
    path("enrolltest/", views.enrolltest, name='enrolltest'),


    # path('posts/<int:pk>/', views.detail, name='detail'),
    # path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
]
