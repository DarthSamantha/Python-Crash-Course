alien_0 = {'colour': 'purple', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"Congrats you just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_postion'] = 25
print(alien_0) 

alien_0['colour'] = 'black'
print(f"The alien is now the colour {alien_0['colour']}")

del alien_0['points']
print(alien_0)


