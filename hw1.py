drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano",
 "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

for key, name in enumerate(drone_list):
  name = name.split(" ")
  name[0] = name[0].capitalize()
  if name[0] == "Dji":
    name[0] = "DJI"
  drone_list[key] = " ".join(name)
  print(drone_list[key])

print()
print("TODO 1")
print()

request = input("Введите производителя: ")

answer_list = list(filter(lambda x: request.lower() in x.lower(), drone_list))

if len(answer_list):
  print("; ".join(answer_list))
  print(f"Количество моделей дронов от данного производителя: {len(answer_list)}")
else:
  print("Нет таких производителей")

print()
print("TODO2")
print()

manufacturer_list = [0]*5
for drone in drone_list:
  if "DJI" in drone:
    manufacturer_list[0]+=1
  elif "Autel" in drone:
    manufacturer_list[1]+=1
  elif "Parrot" in drone:
    manufacturer_list[2]+=1
  elif "Ryze" in drone:
    manufacturer_list[3]+=1
  elif "Eachine" in drone:
    manufacturer_list[4]+=1
manufacturer_names = "DJI Autel Parrot Ryze Eachine".split()
for i in range(len(manufacturer_names)):
  print(f"{manufacturer_names[i]}:{manufacturer_list[i]}")

print()
print("TODO3")
print()

reglist, noreglist = "\n","\n"
reg,no_reg = 0,0

for drone, weight in zip(drone_list,  drone_weight_list):
  if weight > 150:
    reglist += drone + "\n"
    reg += 1
  else:
    noreglist += drone + "\n"
    no_reg += 1
print(f"Регистрируется: {reg}\nНе регистрируется: {no_reg}")
print(f"Список дронов, требующих регистрации: {reglist}")
print(f"Список дронов, не требующих регистрации: {noreglist}")

print("TODO4")
print()

height = int(input("Введите высоту полета (в метрах):"))

inhabited_locality_check = input("Полет проходит над населенным пунктом?[д/н]").lower()
while inhabited_locality_check not in ["д", "н"]: 
  inhabited_locality_check = input("Полет проходит над населенным пунктом?[д/н]").lower()
if inhabited_locality_check == "н": inhabited_locality_check = False

close_zone_check = input("Полет проходит в закрытой зоне?[д/н]").lower()
while close_zone_check not in ["д", "н"]:
  close_zone_check = input("Полет проходит в закрытой зоне?[д/н]").lower()
if close_zone_check == "н": close_zone_check = False

visibility_check = input("Полет проходит в прямой видимости?[д/н]").lower()
while visibility_check not in ["д", "н"]:
  visibility_check = input("Полет проходит в прямой видимости?[д/н]").lower()
if visibility_check == "д": visibility_check = False

for drone, weight in zip(drone_list,  drone_weight_list):
  if (height > 150) or (inhabited_locality_check and weight > 150) or close_zone_check or visibility_check:
      print(f"Полет для дрона '{drone}' при данных условиях обязательно необходимо согласовать")
  else:
      print(f"Полет для дрона '{drone}' не обязательно согласовывать при данных условиях")

print()
print("TODO5")
print()

request = input("Введите производителя: ")

answer_list = list(filter(lambda x: request.lower() in x.lower(),drone_list))

if len(answer_list):
  print(f"Количество моделей дронов от данного производителя: {len(answer_list)}")
  for drone in answer_list:
    drone = drone.split(" ")
    drone.pop(0)
    print(" ".join(drone))
else:
  print("Нет таких производителей")
