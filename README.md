# OsuAI
A personal Python program that uses computer vision and Mouse control packages to play Osu! created by Maxwell Fang. This project is currently still being completed. For those who don't know, Osu! Standard is a free-to-play rhythm game.
The premise is simple. The player selects a song and circles appear on the screen. A larger circle (timing circles) will close in on the previous circle (hit circles) and the objective is to click on every circle when the timing circle meets
the corresponding hit circle. These circles match to different elements of the music hence, why it is considered a rhythm game. A sample can be seen here https://www.youtube.com/watch?v=UYNpkDrCWtA. This is one of the top players in the world.
Neither I nor my program will be nearly as good as he is (likely for runtime reasons).

Currently I am developing the means to click on circles at the right time. Clicking and dragging sliders will come in the near future. I have already designed the approach for the sliders but obviously haven't implemented it. As of now, the following
Python packages are being used in some form: Ultralytics, Numpy, keras, Pytorch, pyautogui, PIL. The current Timing module is using Ultralytics' YOLOv8 to detect circles and keras' Sequential LSTM model (not yet finished) to calculate the right time to click.
The task of detecting circles against a black background isn't that hard and YOLOv8 from my testing thus far seems to be accurate enough so I won't be testing other models (although I may consider once I measure LSTM's runtime). I intend to test the 
LSTM model from Pytorch 2.0 in the future as well since it would cut out approximately 40 ms per Frame captured of processing simply by taking torch tensors as input. Converting the normal output of torch tensors from YOLOv8 to numpy arrays
costs me about 40 ms right now which makes a huge difference in the grand scheme of things.

As of this moment, I am preprocessing the data for the LSTM model and will be training it shortly. I specifically used a similar loop in LSTM_Data_Collection.py as I did in Timing.py to ensure that the model would be trained under similar conditions
that it would be run in. I may also change LSTM_Preprocessing.py to save data into a .csv instead of a .txt using Pandas. This is very simply because it would look more elegant and math students love elegant solutions. It should also be noted that I
do not currently have a model set up to measure the accuracy of the program so that it can improve. I intend to complete this as well but I would prefer to get circles clicked to some extent first.

This is my first time using GitHub so I apologize in advance if anything seems unorganized or unprofessional. I normally work in Jupyter Notebook so some code might be missing where it should be importing from other files.
I also apologize if this isn't particularly what a README is for, I just thought this was the best place to share my thoughts. For any concerns regarding cheating, my program runs solely off of screenshots and does not take information from anywhere else.
I do not intend to use this to cheat nor do I suspect that it will even be better than I am at the game. This is purely for my self-interest and frankly I doubt whether or not I could even write something as capable as Neuro-sama for example.
When I run any code on the game, I am logged out of my account so no pp is gained.

Please share any concerns or feedback to m34fang@uwaterloo.ca
