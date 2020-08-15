import emoji 
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize(':winking_face:', use_aliases=True))
msg = emoji.emojize('Howdy :sun_with_face:')
print(msg)