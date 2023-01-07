def read_int(message = 'Enter the integer number: '):
  valid = False
  while not valid:
    try:
      number = int(input(message))
    except:
      print('>>> ERROR: Enter a integer value.\n')
    else:
      valid = True
  return number

def read_disks(message):
  while True:
    disks = read_int(message)
    if disks > 0:
      return disks
    print(f'>>> ERROR: Can\'t do anything with {disks} disks.\n')
