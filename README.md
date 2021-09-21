# Mastermind

This is a game I made in Python 3 using Tkinter in _Informatique et Sciences du Numérique_ (a french computer oriented discipline) for the Baccalauréat Scientifique (the french national academic qualification) in 2018.

## Screenshots

<p align="center">
  <img src="https://i.imgur.com/TjwjTCK.png" width="415" />
  <img src="https://i.imgur.com/3HiEb30.png" width="415" />
  <img src="https://i.imgur.com/AJDPQtA.png" width="415" />
  <img src="https://i.imgur.com/XaNuA64.png" width="415" />
</p>

## How to run

### Prerequisites

Install [Python 3 or earlier](https://www.python.org/downloads/) and pip.

Then, install Tkinter.

On Windows, it should be pre-installed with Python 3.

On Debian-based Linux distributions, install it with :

```
sudo apt-get install -y python3-tk
```

On RedHat-based Linux distributions, install it with :

```
sudo dnf install -y python3-tkinter
```

Then install pyglet with :

```
pip install pyglet
```

If you do not wish to install pyglet, then set the `ACTIVER_EFFETS_SONORES` variable to `False` at the beginning of the code of `mastermind.py` file.

### Run

Simply run :

```
python mastermind.py
```

## Credits

- Backgrounds : [AxiomDesign](https://www.deviantart.com/axiomdesign)
- Fonts : [Streamster](https://www.dafont.com/streamster.font), [Death Star](https://www.dafont.com/death-star.font) and [Krinkes](https://www.dafont.com/krinkes.font)
- Sound effects : GTA: San Andreas, [zapsplat.com](https://www.zapsplat.com)
- Sprites : I made all the sprites with Photoshop CC 2017, psd source files are available [here](https://github.com/plcharriere/mastermind.py/tree/main/ressources/images/sources%20psd).