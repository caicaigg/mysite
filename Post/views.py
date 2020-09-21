from django.shortcuts import render

# Create your views here.
def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request=request, template_name='Post/index.html')

def helloworld(request):
    print("你进来了啊")
    return render(request, 'Post/a.html')

def reg(request):
    print("注册中....")
    name = request.POST.get('username');
    password = request.POST.get('password');
    print('用户名:', name, ' 密码:', password)
    return render(request, 'Post/success.html',{'name':name})

def save(request):
    print("保存表格")
    if request.method == 'post':
        cell0=request.POST.get('cell0');
        cell1=request.POST.get('cell1');
        print('cell0:',cell0,'cell1:',cell1);
    else:
        print("method is no post");
    return render(request, 'Post/index.html')

def success(request):
    result = ""
    for k, v in request.GET.items():
        result = v
    print("result:", result)
    return render(request, 'success.html', {'username': result})

