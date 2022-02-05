from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View







class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
                postdata=request.POST
                first_name=postdata.get('firstname')
                last_name=postdata.get('last name')
                phone=postdata.get('phone')
                email1=postdata.get('email')
                password=postdata.get('password')


                value={'first_name':first_name,'last_name':last_name,
                        'phone':phone,'email':email1}
                customer=Customer(first_name=first_name,
                                   last_name=last_name,
                                   phone_no=phone,
                                   email=email1,
                                   password=password)
                error_massage=self.validation(customer)
                if not error_massage:

                    customer.password=make_password(customer.password)
                    customer.register()
                    return redirect('homepage')
                else:
                    data={'error':error_massage,
                           'values':value}
                    return render(request,'signup.html',data)


    def validation(self,customer):
        def isExist(checkmail):
            if Customer.objects.filter(email=checkmail):
                return True
            return False

        error_massage=None
        if(not customer.first_name) :
            error_massage="First name must be required"
        elif len(customer.first_name)<4 :
            error_massage="First Name Should be atleast 4 character"
        elif(not customer.last_name):
            error_massage="Last name must be required"
        elif len(customer.last_name)<4:
            error_massage="last Name Should be atleast 4 character"
        if(not customer.phone_no) :
            error_massage="must be required phone no"
        elif len(customer.phone_no)>12 :
            error_massage="phone_no Should be hould atleast 10 digit"
        elif(not customer.email):
            error_massage="mail must be required"
        elif len(customer.email)<5:
            error_massage="email Should be proper legth"
        elif(not customer.password):
                error_massage="password Must be required"
        elif len(customer.password)<4:
             error_massage="password must be 6 digit"
        elif isExist(customer.email):
             error_massage="Email Already isExist"
        return error_massage
