rawr
====

.. list-table::
   :widths: auto
   :align: center

   * - |actions-pypi|
     - |actions-reqs|
     - |actions-fmt|

This is a simple CLI for using rarbgapi__ to find a torrent,
then start fetching it with aria2__.

__ https://github.com/verybada/rarbgapi

__ http://aria2.sourceforge.net/

Usage
-----

.. code:: console

  $ rawr gold rush 1925

.. image:: https://user-images.githubusercontent.com/1787385/94336947-c30fa500-ffb4-11ea-8687-126a16779bfe.png
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

.. code:: console

  % pipz install --cmd rawr rawr-cli


.. |actions-fmt| image:: https://github.com/AndydeCleyre/rawr/actions/workflows/fmt.yml/badge.svg?branch=develop
   :alt: Automated Code Format Status
   :target: https://github.com/AndydeCleyre/rawr/actions/workflows/fmt.yml

.. |actions-pypi| image:: https://github.com/AndydeCleyre/rawr/actions/workflows/pypi-release.yml/badge.svg?branch=master
   :alt: Automated PyPI Release Status
   :target: https://github.com/AndydeCleyre/rawr/actions/workflows/pypi-release.yml

.. |actions-reqs| image:: https://github.com/AndydeCleyre/rawr/actions/workflows/reqs.yml/badge.svg?branch=develop
   :alt: Automated Python Requirements Bump Status
   :target: https://github.com/AndydeCleyre/rawr/actions/workflows/reqs.yml
