import random
time=["A long time ago ",'Once upon a time ','Last year ','A thousand years ago ','Before the birth of animals ','At the time of apocalypse ']
place=['in the middle of the woods ','near the lake ','at the park ','under the ocean ','below the earth ','in the sky ','above the roof of the house ',
       'over the top of the mountains ','under the oldest tree in existence ','inside a closed dark room ','in the space ','on the moon ',]
person=['Ironman ','Batman ','Spiderman ','Superwoman ','She-hulk ','Po ','Catwoman ','Dr.Strange ','Spiderman ','Sheldon ','Ella ','Mako ','Bodvar ']
verb=['was reading a ','was writing a','was hiding a ','was firing up a ','was mining a ','was showering a ','was hiding in a',
      'was rolling a ','was making a ','was lifting a ','was dancing with a ','was playing with a ','was eating a ']
thing=['cat.','banana.','sword.','glass.','wine.','lamp.','mask.','coin.','book.','alien.','laptop.','metal disc.','boiled egg.',
       'hammer.','screw.','plant.','clothes.','lighthouse.','cycle.','deck of cards.','lighntining bolt.']
print(random.choice(time)+random.choice(place)+random.choice(person)+random.choice(verb)+random.choice(thing))
