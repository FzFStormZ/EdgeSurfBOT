# EdgeSurfBOT

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)

EdgeSurfBOT is a little project based on the game "surf" of the Edge browser.

<img src=imgs/Demonstration.gif width="700px" height="400px" alt="How to run a game"/>

## How works ❔

First, my code based on the **High visibility mode** which allow to see rectangles around each objects on the game.
With that, I can know if the surfer going to an obstacle, a boost or whatever in the game.
To detect obstacles, I build rectangles around the surfer to take decision in function of what is in each rectangles:

<img src=imgs/ExplanationREADME.png width="550px" height="600px" alt="My rectangles"/>

In this game, we have color code which is:
* **Black objects**: They are dangerous for the surfer. They stop him and he loses 1 ❤️.
* **Red objects**: They aren't dangerous but slow down the surfer.
* **Green ojects**: They allow to take a ⚡ boost or a springboard in goal to gain a speed boost.


## Requirements

- Python 3
- New Microsoft Edge browser ❤️

## Dependencies

- PyAutoGui : <https://pypi.org/project/PyAutoGUI>
- Numpy : <https://pypi.org/project/numpy/>

## Quick Start

1. Clone the latest version of Volatility from GitHub:

    ```shell
    git clone https://github.com/FzFStormZ/EdgeSurfBOT.git
    ```

2. Go on your Edge browser and put this link below on your navigation bar:

    ```shell
    edge://surf
    ```

3. Choose the same settings than me:

    <img src=imgs/Parameters.PNG width="300px" height="400px" alt="How to run a game"/>

    _Explain:_
    + **Let's surf** : Principal game mode
    + **High visibility mode** allow to see rectangles around each objects on the game
    + **Reduced speed mode** allow to take decision more easily

4. ⚠️ __WARNING__ ⚠️ Split your screen between the browser and your CMD such as :

    <img src=imgs/ExampleStartProject.PNG width="700px" height="400px" alt="How to run a game"/>

## Versions

**Last version :** 2.0
List of versions : [Click to show them](https://github.com/FzFStormZ/EdgeSurfBOT/tags)

## TO DO

* Detect red obstacles.
* Box to find quickly a boost (after 1000 meters).
* Fix the fact that the surfer not continue after down by black object.
* Decisional conditions to machine learning (after a complete decisional conditions project).

## Authors

* **FzF_StormZ**:
  + My GitHub: <https://github.com/FzFStormZ>
  + My YouTube channel: <https://www.youtube.com/channel/UCFokPE7IzGVhwQeIBmja7ew>
  + My Discord server: <https://discord.gg/WSe9WvG>

## Licence

This project haven't a licence

## Others

[Pretty badges for your Git project](https://forthebadge.com/)
[Some emojis to complete my README file 😜](https://gist.github.com/rxaviers/7360908)
