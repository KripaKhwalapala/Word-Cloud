from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Define the words
words = """
Quiet corners, Mystic trance, Eyes like deep seas, Silent grace, Solitude, Solace , Sacred Ground, A labyrinth unknown, Tale of dreams, Paradox , Echoes, Whispered secret, Stillness of night, Moonbeams , Stars, Song, Riddles , Language of soul, Symphony, Muse
""".split()

# Join the words into a single string
text = ' '.join(words)

# Load an image to use as the shape of the word cloud (girl's face with a flower crown)
girl_mask = np.array(Image.open("girl_face1.jpg"))

# Create the word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='cividis', mask=girl_mask).generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
