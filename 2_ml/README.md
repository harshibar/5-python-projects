# I Taught an AI to Play Ping Pong 🏓
#### 5 Python Projects in 5 Days - Day 2: Machine Learning

An exploration of how to use OpenAI Gym to teach an AI to play games, from basic tasks like Mountain Car, to Atari Pong.

#### Mountain Car:
![mountain car](/2_ml/car.gif)

#### Atari Pong:
![mountain car](/2_ml/pong.gif)

**📸YouTube Tutorial: [https://www.youtube.com/harshibar](https://www.youtube.com/harshibar)**

## Inspiration
I took one Machine Learning class in school, but even after that, I never really branched out in my ML projects beyond plugging in some SciKitLearn packages and crossing my fingers. So, for this project, I wanted to learn something way out of my comfort zone, even if it meant that I couldn't create something completely original. So, I spent a day learning about reinforcement learning and Deep Q Learning, and taught an AI to play some games (with a lot of help). 🙏🏾

## Installation
1. Follow the instructions for installing OpenAI Gym [here](https://gym.openai.com/docs). You may need to install `cmake` first.
2. Install NumPy: `pip install numpy`
3. Install TensorFlow: `pip install tensorflow`
4. Install Keras: `pip install keras`

## Usage
#### To run the mountain car example (this takes around 20 minutes to train)
    $ python mountain-car.py

#### To run the mountain car example (this takes 3-5 days to train)
    $ python pingpong.py

#### To see results:
The [scores](/2_ml/scores/score_logger.py) folder has some tools to plot the results of an exercise, and can be customized further.

## Thanks

* [Deep Q Learning Starter Code](https://github.com/gsurma/cartpole) - Starter code that I used for the Mountain Car example based on the previous article
* [Atari Pong Starter Code](https://github.com/dhruvp/atari-pong) - Code from the author of the previous article on how to implement an AI for Pong

## Learn More

* [Deep Q Learning Article](https://keon.github.io/deep-q-learning/) - A grat article I used to implement the Mountain Car example and learn about Deep Q Learning (DQN)
* [Reinforcement Learning for Atari Pong Article](https://medium.com/@dhruvp/how-to-write-a-neural-network-to-play-pong-from-scratch-956b57d4f6e0) - A great overview of how to use reinforcement learning to teach an AI to play Pong
* [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/) - A more in-depth article on the previous topic

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/harshibar/5-python-projects/blob/master/LICENSE) file for details.