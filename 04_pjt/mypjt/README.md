1. 학습한 내용
    - ex) movies/models.py(movies어플에서)
        - models을 작성하거나 수정 후 makemigrations를 해줘야 함 - 후에 migrate!
    - ex) movies/urls.py(movies어플에서)목록의 값이 필요한 경로일 경우:  <ink:pk>가 필요!
        - path(’<int:pk>/update/’, views.update, name=’update’
    - 이미지를 받아오려면 터미널에서 ‘pip install pillow’를 해야함
        - load static을 필수로 해줘야 함
        - img src=”{% static ‘image.jpg’ %} static으로 이미지 가져와야함
    - 함수를 호출하려면 (:) / 경로로 이동하려면 (/)
    - views에서 require_POST = 'POST' / require_safe = 'GET' / require_http_methods = 'GET' & 'POST’
    - create, delete, update 등등과 같은 친구들은 값이 생김!
        - 값이 생기는 함수면 views에서 pk=[movie.pk](http://movie.pk) 를 작성해주기.
        
        ```
        # movies/views.py
        @require_http_methods(['GET', 'POST'])
        def create(request):
            if request.method == 'POST':
                form = MovieForm(request.POST, request.FILES)
                if form.is_valid():
                    movie = form.save()
                    return redirect('movies:detail', pk=movie.pk)
            else:
                form = MovieForm()
            context = {'form': form}
            return render(request, 'movies/create.html', context)
        ```
        
        - 값을 가져와야 하는 함수면 views에서 movie = Movie.objects.get(pk=pk) 이런 식으로 get 함수에 pk값 넣어주기
        
        ```jsx
        # movies/views.py
        @require_safe
        def detail(request, pk):
            movie = get_object_or_404(Movie, pk=pk)
            movie = Movie.objects.get(pk=pk)
            context = {'movie':movie}
            return render(request, 'movies/detail.html', context)
        ```
        
        - 해당 html로 가서 연결하려는 링크에 ‘movies:update’ movie.pk 이런 식으로 값을 넣어줘야 함!! 중요!!
            - create는 생성만 하는 기능이기에 링크에 값 넣어줄 필요 x
            - 값이 필요한 함수에만 해주면 ok
            
            ```jsx
            # movies/update.html
            {% extends 'base.html' %} 
            
            {% block content %}
              <h1>UPDATE</h1>
              <hr />
            
              <form action="{% url 'movies:update' movie.pk %}" method="POST"  enctype='multipart/form-data'>
                {% csrf_token %} {{form.as_p}}
                <input type="submit" value="SUBMIT">
              </form>
            
              <hr />
              <a href="{% url 'movies:index' %}">BACK</a>
            {% endblock content %}
            ```
            
    - 생성, 수정, 삭제 등 값이 변하는 경우에는 해당 함수 작성하는 블럭 안에{% csrf_token %} 을 넣어줘야 함.
    
2. 어려웠던 부분
    - 오류가 떴을 때 어디가 문제인지 찾기가 어렵다
    - 경로를 엮기가 은근히 헷갈린다
    - 어떤 것은 값(pk)을 넣어줘야 하는지, 어떤 것은 필요가 없는지 구분하기가 힘들다
3. 느낀 점
    - 경로를 잘 보자!
    - 오류 해석을 잘 하자
    - 오타를 조심하자
    - 값의 이름을 잘 보자! (ex. movies 인지 movie 인지)