Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> from numpy import *
    x = linspace(0, 7, 70)
    y = cos(x)
    
>>> from matplotlib import pyplot as plt

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
>>> plt.grid()
>>> plt.xlabel('x')
<matplotlib.text.Text object at 0x7f3fb7845e10>
>>> plt.ylabel('f(x)')
<matplotlib.text.Text object at 0x7f3fb786ad50>
>>> 
======================== RESTART: /home/user/1b12.py ========================

======================== RESTART: /home/user/1b12.py ========================

======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RRGGBB"
to_rgb: Invalid rgb arg "#RRGGBB"
invalid hex color string "#rrggbb"
>>> 
======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RR"
to_rgb: Invalid rgb arg "#RR"
invalid hex color string "#rr"
>>> 
======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RRGGBB"
to_rgb: Invalid rgb arg "#RRGGBB"
invalid hex color string "#rrggbb"
>>> 
======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RRGGBB"
to_rgb: Invalid rgb arg "#RRGGBB"
invalid hex color string "#rrggbb"
>>> 
======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RRGGBB"
to_rgb: Invalid rgb arg "#RRGGBB"
invalid hex color string "#rrggbb"
>>> 
======================== RESTART: /home/user/1b12.py ========================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 283, in resize
    self.show()
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_tkagg.py", line 354, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/python2.7/dist-packages/matplotlib/backends/backend_agg.py", line 474, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/figure.py", line 1159, in draw
    func(*args)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_base.py", line 2324, in draw
    a.draw(renderer)
  File "/usr/lib/python2.7/dist-packages/matplotlib/artist.py", line 61, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 739, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/lib/python2.7/dist-packages/matplotlib/lines.py", line 1251, in _get_rgba_ln_color
    return colorConverter.to_rgba(self._color, self._alpha)
  File "/usr/lib/python2.7/dist-packages/matplotlib/colors.py", line 376, in to_rgba
    'to_rgba: Invalid rgba arg "%s"\n%s' % (str(arg), exc))
ValueError: to_rgba: Invalid rgba arg "#RRGGBB"
to_rgb: Invalid rgb arg "#RRGGBB"
invalid hex color string "#rrggbb"
>>> 
======================== RESTART: /home/user/1b12.py ========================
>>> 
======================== RESTART: /home/user/1b12.py ========================

======================== RESTART: /home/user/1B1.pyy ========================
>>> 
======================== RESTART: /home/user/1B11.py ========================
>>> 
======================== RESTART: /home/user/1B11.py ========================
>>> 
========================= RESTART: /home/user/1B2.py =========================
>>> 
========================= RESTART: /home/user/1B2.py =========================
>>> 
======================== RESTART: /home/user/1B11.py ========================
>>> 
======================== RESTART: /home/user/1B11.py ========================
>>> 
========================= RESTART: /home/user/1B2.py =========================

========================= RESTART: /home/user/1B2.py =========================
>>> 
