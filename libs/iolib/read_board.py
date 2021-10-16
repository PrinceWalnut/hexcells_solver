"""
This file is meant to read the initial game state from Hexcells.
It will then be store as a 2D wavy array of cells that are either blue, grey (with neighbor numbers), or grey (no info).
Vertical and diagonal row numbers will be treated as a group data structure, along with any special rules (e.g. contiguous blue cells).
Data will be written to /game_states/ as a numpy array file.
"""
