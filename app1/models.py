from django.db import models
from django_jalali.db import models as jmodels


class StudentClass(models.Model):
    cname=models.CharField(max_length=20,verbose_name=" اسم کلاس")
    code=models.CharField(max_length=10,verbose_name="کد کلاس ")
    createdRecord=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name="کلاس "
        verbose_name_plural="کلاسها "
        
    def __str__(self):
        return f"{self.cname}"


class Student(models.Model):
    classname=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    fname=models.CharField(max_length=30,verbose_name=" نام")
    lname=models.CharField(max_length=50,verbose_name="نام خانوادگی ")
    fullname=models.CharField(max_length=70,blank=True,editable=False)
    gender_list=(True,"مرد"),(False,"زن"),
    gender=models.BooleanField(choices=gender_list,verbose_name="جنسیت",default=True)
    phone=models.CharField(max_length=11,blank=True)
    edu_list=("Diploma","دیپلم"),("Ac","تکنیسین"),("BSc","کارشناسی"),("MSc","کارشناسی ارشد"),("PHd","دکترا")
    edu=models.CharField(max_length=10,choices=edu_list,blank=True,verbose_name="مدرک تحصیلی")
    dob=jmodels.jDateField(verbose_name="تاریخ تولد")
    createdRecord=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name="دانشجو"
        verbose_name_plural="دانشجوها"
        
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    def save(self,*args,**kwarg):
        self.fullname=f"{self.fname} {self.lname}"
        super(Student,self).save(*args,**kwarg)
        
        
    
    
    
    