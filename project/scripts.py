from datacenter.models import Schoolkid,Mark,Chastisement

def fixed_mark(schoolkid:Schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid,points__range=(0,3))
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()

def remove_chastisements(schoolkid:Schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()

def create_commendation(name,subject):
    pass

