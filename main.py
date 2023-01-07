from reading import read_disks
from tower_of_hanoi import tower_of_hanoi

towers = {
  'begin': 'A',
  'middle': 'B',
  'end': 'C',
  'disks': 0
}

towers['disks'] = read_disks('Enter the number of disks: ')

print(f'\n{" INFORMATIONS ":=^35}')
for key, value in towers.items():
  print(f'{key.capitalize():.<10}{value:.>25}')

print(f'\n{" SOLVING THE TOWER OF HANOI ":=^35}')
tower_of_hanoi(towers['disks'], towers['begin'], towers['middle'], towers['end'])
