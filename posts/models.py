from django.db import models
from embed_video.fields import EmbedVideoField

 
class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)
    field = models.URLField(max_length=200)



class Post1(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)
    slug = models.SlugField()
   
    def __str__(self):
        return self.title
 
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    
 
    def __str__(self):
        return self.post.title


class Box1(models.Model):
 
    BOX_BIG_SIZES = (
           
            ('240х185х120', '240х185х120'),
            ('270х220х70', '270х220х70'),
        )
  

    box_size1 = models.CharField(max_length=20, choices=BOX_BIG_SIZES,default='80х80х40')
    tirazh1 = models.IntegerField(null=False)
 

class Box(models.Model):

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Box, self).save(*args, **kwargs)
 
    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
  


    BOX_SIZES = (
                ('50х50х35', '50х50х35'),
                ('60х60х40', '60х60х40'),
                ('60х60х40-P', '60х60х40-P'),
                ('80х80х40', '80х80х40'),
                ('80х80х40-P', '80х80х40-P'),
                ('240х185х120', '240х185х120'),
                ('270х220х70', '270х220х70'),
            
          
        )
    

    # Модель в методе save при сохранении объекта автоматически удаляет все остальные, что позволяет держать в базее данных всегда только один экземпляр данной модели.

    # Метод load берёт из базы данных то единственный объект настроек, если же объект не существует в базе данных, то возвращает новый инстанс этой модели, который нужно будет потом сохранить.
 
   

    box_size = models.CharField(max_length=20, choices=BOX_SIZES,default='80х80х40')
    tirazh = models.IntegerField(null=False)
      
   
   
    # get_cost размер 270х220х70 мм ручная сборка 
    
    def get_cost(self):


        a =(176.3969+17367.3469/self.tirazh)*self.tirazh
        
        return "{0:.2f}".format(round(a,0))
    
   
    def ret(request):
        

        all_result = Box.objects.all()
        result_one = all_result.filter(box_size ='50х50х35')
        result_two = all_result.filter(box_size ='60х60х40')
        result_three = all_result.filter(box_size ='80х80х40')
        result_four = all_result.filter(box_size ='60х60х40-P')
        result_five = all_result.filter(box_size ='80х80х40-P')
        result_six = all_result.filter(box_size ='240х185х120')
        result_seven = all_result.filter(box_size ='270х220х70')

       
    
        if result_one:
            
            return  3935428.2860 # 50х50х35 крышка-дно, сборка на автомат от 2500 шт
        elif  result_two:
            return 2560787.2222  # 60x60x40 крышка-дно, сборка на автомат от 2500 шт
        elif  result_three:
            return 2230289.1977  # 80х80х40 крышка-дно, сборка на автомат от 2500 шт  

        elif  result_four:
            return 2642166.1889  # 60x60x40 крышка-дно-поясок, сборка на автомат от 2500 шт
        elif  result_five:
            return 2248996.1600 # 224.8996x−0.1600 80х80х40 крышка-дно-поясок, сборка на автомат от 2500 шт
        
        elif  result_six:
            return 10780131.2554 # размер 240х185х120 мм ручная сборка    
        
        elif  result_seven:
            return 7799003.1669 # размер 270х220х70 мм ручная сборка y=779.9003x−0.1669

        else:
            return 0

  
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



  
