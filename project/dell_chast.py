from datacenter.models import Schoolkid,Chastisement

def remove_chastisements(schoolkid:Schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()