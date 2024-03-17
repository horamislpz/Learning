
def send_mail (num_visits, visits_email, visit_coupon):
    if visits_email >= num_visits:
        print("Not enough visits.")
    elif num_visits >= visit_coupon:
        print("Send Email with coupon")
    else:
        print("Send Email.")
        
send_mail(num_visits=6,visits_email=3, visit_coupon=2)
