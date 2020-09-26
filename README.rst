rawr
====

This is a simple CLI for using rarbgapi__ to find a torrent,
then start fetching it with aria2__.

__ https://github.com/verybada/rarbgapi

__ http://aria2.sourceforge.net/

Usage
-----

.. code:: console

  $ rawr gold rush 1925

.. image:: https://user-images.githubusercontent.com/1787385/94319181-17d10280-ff58-11ea-99a1-f56e2ff5ddd1.png
   :alt: Screenshot: rawr gold rush 1925

All categories will be searched, excepting ADULT.
To invert that behavior, pass ``-a``.

Requirements
------------

In addition to Python >=3.6, and the modules ``pip`` gets for you during Install_:

- ``rawr`` needs ``aria2c`` in the ``PATH`` if you want it to start a download for you.

- Before beginning a download, ``rawr`` will show some info about your connection,
  using the first method whose required command(s) are detected, checking in this order:

  - ``mullvad``
  - ``nmcli`` and ``grep``
  - ``https`` (httpie__)
  - ``curl``
  - ``wget``

- If ``xclip`` or ``pbcopy`` are found,
  the chosen magnet URI will be copied to the clipboard.

- If ``df`` is found, you will get a notice about your hardware's free space
  when showing search results.

__ https://httpie.org/

Install
-------

Method 1: pip, user-level
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: console

  $ pip3 install --user rawr-cli

Method 2: pipx
~~~~~~~~~~~~~~

pipx__ can help you install tools from PyPI into isolated venvs:

__ https://pipxproject.github.io/pipx/installation/

.. code:: console

  $ pipx install rawr-cli

Method 3: zpy
~~~~~~~~~~~~~

zpy__ can also help you install tools from PyPI into isolated venvs, with ``pipz``:

__ https://github.com/andydecleyre/zpy

.. code:: zsh

  % pipz install rawr-cli
