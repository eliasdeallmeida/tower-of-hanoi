def tower_of_hanoi(disks, begin, middle, end):
  if disks > 0:
    tower_of_hanoi(disks - 1, begin, end, middle)
    print(f'Move disk {disks} from {begin} to {end}')
    tower_of_hanoi(disks - 1, middle, begin, end)
