tahta =[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def kazanan(tahta, oyuncu):
 kazanma_durum ={
        '1': [(0,0), (0,1), (0,2)],
        '2': [(0,0), (1,1), (2,2)],
        '3': [(0,0), (1,0), (2,0)],
        '4': [(0,1), (1,1), (2,1)],
        '5': [(0,2), (1,1), (2,0)],
        '6': [(0,2), (1,2), (2,2)],
        '7': [(1,0), (1,1), (1,2)],
        '8': [(2,0), (2,1), (2,2)]
        }
 for durum in kazanma_durum.values():
     kazan = True
     for sat,sut in durum:
        if tahta[sat][sut] != oyuncu:
           kazan = False
           break
     if kazan == True:
        return True
 return False 



def tahta_yazdirmak(tahta):
  for satir in tahta:
        print(" | ".join(satir))
        print("-" * 9)
#tahat_yazdirmak(tahta)

#tahta_yazdirmak(tahta)
def full_dolu(tahta):
   for bos in tahta:
       for boskume in bos:
          if boskume == ' ':
             return False
   return True

def oyun():
 try:
  suan_oyuncu = 'X'
  while True:
    tahta_yazdirmak(tahta)
    
    satir = int(input(f"Oyuncu {suan_oyuncu}, satir degeriniz(0,1,2): "))
    sutun = int(input(f"Oyuncu {suan_oyuncu}, sutun degeriniz(0,1,2): "))

    if satir not in  [0,1,2] or sutun not in [0,1,2]:
      print("Yanlis sayi girdiniz")
      continue
     
    if tahta[satir][sutun] == ' ':
      tahta[satir][sutun] = suan_oyuncu
      if kazanan(tahta, suan_oyuncu):
         tahta_yazdirmak(tahta)
         print(f"Sen kazandin: {suan_oyuncu}")
         break
      if full_dolu(tahta):
         tahta_yazdirmak(tahta)
         print ("Berabere")
         break
      if suan_oyuncu == 'X':
         suan_oyuncu = 'O'
      else:
         suan_oyuncu = 'X'
    else:
       print(("\n"),"Burasi dolu tekrar giriniz",("\n"))
       #print()
 except ValueError:
    print("Lutfen harf ya da ozel harf girmeyin")        
    oyun()       
oyun()