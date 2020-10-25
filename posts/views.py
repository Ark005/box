from django.views.generic import ListView,DetailView
from .models import Post,Box,PostImage,Post1,Box1
from django.http import JsonResponse
from django.core import serializers
from .forms import BoxForm,Box1Form
from django.views import View
from django.shortcuts import render, get_object_or_404

def production_view(request):
    return render(request, 'production.html')

 
def detail_view(request, id):
    post = get_object_or_404(Url, id=id)
    #post = get_object_or_404(Post, pk=pk)
    #return render(request, 'blog/post_detail.html', {'post': post})
    #photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'field':field,
       
    })

def contacts_view(request):
    return render(request, 'contacts.html') 

def about_view(request):
    return render(request, 'about.html')

def home_view(request):
    #posts = Post.objects.get(title="t1") 
    #posts = Post.objects.all()
    return render(request, 'home.html')    #,{'posts':posts})
 
def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})
 
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })

def blog1_view(request):
    posts = Post.objects.all()
    return render(request, 'product.detail.html', {'posts':posts})



'''

class BoksView(DetailView):
    template_name = "box.html"

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(boxView, self).get_context_data(**kwargs)
        # Get Related publishers
        context['boxes'] = self.object.boxes.filter(is_active=True)
        return context


'''


def boxView(request):
    form =  BoxForm()
    boxes = Box.objects.all()
    return render(request, "box.html", {"form": form, "boxes": boxes})

def boxView1(request):
    form = BoxForm()
    boxes = Box.objects.all()
    return render(request, "box1.html", {"form": form, "boxes": boxes})

def boxView2(request):
    form = BoxForm()
    boxes = Box.objects.all()
    return render(request, "box2.html", {"form": form, "boxes": boxes})

def boxView3(request):
    form = BoxForm()
    boxes = Box.objects.all()
    return render(request, "box3.html", {"form": form, "boxes": boxes})

def boxView4(request):
    form = BoxForm()
    boxes = Box.objects.all()
    return render(request, "box4.html", {"form": form, "boxes": boxes})

def boxView5(request):
    form = BoxForm()
    boxes = Box.objects.all()
    return render(request, "box5.html", {"form": form, "boxes": boxes})


def postBox(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = BoxForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

# BONUS CBV
def checkNickName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if Friend.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    


class BoxView(View):
    form_class = BoxForm
    template_name = "box.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        boxes = Box.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "boxes": boxes})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)
class BoxView1(View):
    form_class = BoxForm
    template_name = "box1.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        boxes = Box.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "boxes": boxes})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })