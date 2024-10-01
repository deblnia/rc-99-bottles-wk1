class BottleVerse:
  
  def lyrics(num):
    return (
      f'{num} bottles of beer on the wall, '
      f'{num} bottles of beer.\n'
      f'Take {"one" if num >= 2 else "it"} down and pass it around, '
      f'{num-1 if num >= 2 else "no more"} bottle{"s" if num != 2 else ""} of beer on the wall.\n'
    )